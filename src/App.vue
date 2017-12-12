<template>
  <!-- Don't drop "q-app" class -->
  <div id="q-app">
    <q-layout ref="layout" view="Lhh lpr lFf">
      <q-toolbar slot="header"
                 class="row items-center relative-position q-toolbar-normal fixed-top"
                 :class="'bg-'+this.color" v-ripple>
        <q-toolbar-title id="title">
          优先队列
        </q-toolbar-title>
      </q-toolbar>
      <router-view/>
      <footer class="fixed-bottom">
        <q-tabs position="bottom">
          <q-tab slot="title" name="tab-1" icon="alarm on" label="目前任务" @select="$router.push('/')" default/>
          <q-tab slot="title" name="tab-2" icon="list" label="任务列表" @select="$router.push('/list')"/>
        </q-tabs>
      </footer>
    </q-layout>
  </div>
</template>

<script>
  import {
    QLayout,
    QToolbar,
    QToolbarTitle,
    Ripple,
    QTabs,
    QTab
  } from 'quasar'

  export default {
    directives: {
      Ripple
    },
    components: {
      QLayout,
      QToolbar,
      QToolbarTitle,
      QTabs,
      QTab
    }
  }
</script>

<style lang="stylus" scoped>
  @import '~variables'
  #q-app {
    max-height: 100vh
    overflow: hidden
    padding-top: 100px
    padding-bottom: 48px
  }
</style>
