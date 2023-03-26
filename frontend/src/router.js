import Vue from 'vue';
import VueRouter from 'vue-router';
import { createProvider } from '@/apollo';

import Main from '@/components/Main.vue';
import AuthView from '@/components/auth/AuthView.vue';
import OrganizationCreateView from '@/components/organization/OrganizationCreateView.vue';
import RoomPlayground from '@/components/room/playground/RoomPlayground.vue';
import SignUpView from '@/components/auth/SignUpView.vue';
import SignUpConfirmView from '@/components/auth/SignUpCofirmView.vue';

import store from '@/store.js';
import {
  MAIN_PATH,
  AUTH_PATH,
  NEW_ORGANIZATION_PATH,
  ROOMS_ROOT_PATH,
  SIGN_UP_PATH,
  SIGN_UP_CONFIRM_PATH,
} from '@/pathVariables.js';

import verifyToken from '@/graphql/mutations/verifyToken.gql';
import profile from '@/graphql/queries/profile.gql';

export function verifyAuth(to, from) {
  store.commit('START_LOADING');
  let provider = createProvider();
  return new Promise(function (resolve, reject) {
    provider.defaultClient
      .mutate({ mutation: verifyToken })
      .then((result) => {
        let userId = result.data.verifyToken.payload.user_id;
        store.commit('SET_USER_ID', userId);
        store.commit('SET_IS_AUTHENTICATED', true);
        setProfile(provider, userId);
      })
      .catch((error) => {
        store.commit('SET_IS_AUTHENTICATED', false);
      })
      .finally(() => {
        store.commit('SET_GOT_VERIFIED_AUTH', true);
        store.commit('STOP_LOADING');
        resolve();
      });
  });
}

async function setProfile(provider, userId) {
  return new Promise(function (resolve, reject) {
    provider.defaultClient
      .mutate({ mutation: profile })
      .then((result) => {
        store.commit('SET_USER_NAME', result.data.profile.firstName + " " + result.data.profile.lastName);
      })
  });
}

const ifAuthenticated = async (to, from, next) => {
  try {
    if (!store.state.gotVerifiedAuth) {
      await verifyAuth(to, from);
    }
    if (store.state.isAuthenticated) {
      next();
      return;
    }
    next(AUTH_PATH);
  } catch (error) {
    console.log('ERROR TEST: ', error);
  }
};

const ifNotAuthenticated = async (to, from, next) => {
  try {
    if (!store.state.gotVerifiedAuth) {
      await verifyAuth(to, from);
    }
    if (!store.state.isAuthenticated) {
      next();
      return;
    }
    next(MAIN_PATH);
  } catch (error) {
    console.log('ERROR TEST: ', error);
  }
};

const routes = [
  {
    path: '',
    component: Main,
    beforeEnter: ifAuthenticated,
    meta: { title: 'Главная - ImGames' },
  },
  {
    path: AUTH_PATH,
    component: AuthView,
    beforeEnter: ifNotAuthenticated,
    meta: { title: 'Войти - ImGames' },
  },
  {
    path: SIGN_UP_PATH,
    component: SignUpView,
    beforeEnter: ifNotAuthenticated,
    meta: { title: 'Зарегистрироваться - ImGames' },
  },
  {
    path: NEW_ORGANIZATION_PATH,
    component: OrganizationCreateView,
    beforeEnter: ifAuthenticated,
    meta: { title: 'Создать пространство - ImGames' },
  },
  {
    path: ROOMS_ROOT_PATH + '/:roomCode',
    component: RoomPlayground,
    beforeEnter: ifAuthenticated,
    meta: { title: 'Игровая комната' },
  },
  {
    path: SIGN_UP_CONFIRM_PATH + '/:token',
    component: SignUpConfirmView,
    beforeEnter: ifNotAuthenticated,
    meta: { title: 'Подтверждение регистрации' },
  },
];

Vue.use(VueRouter);
const router = new VueRouter({
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  },
  mode: 'history',
  routes,
});

export default router;
