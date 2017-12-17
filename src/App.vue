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

  const colors = ['primary', 'amber', 'secondary', 'orange', 'tertiary', 'lime', 'cyan', 'purple', 'brown', 'blue']
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
    },
    data () {
      return {
        color: colors[0],
        index: 0
      }
    },
    mounted () {
      this.timer = setInterval(() => {
        this.index = (this.index + 1) % colors.length
        this.color = colors[this.index]
      }, 2000)
    }
  }
</script>

<style lang="stylus">
  @import '~variables'
  #q-app {
    max-height: 100vh
    overflow: hidden
    padding-top: 100px
    padding-bottom: 48px
  }

  .q-toolbar {
    height: 100px
    text-align: center
    transition: background 2.5s
    cursor: default
    .q-toolbar-title {
      font-size: 30pt
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif
    }
    -webkit-user-select: none
    -moz-user-select: none
  }

  .q-tabs-bar {
    color: $pink-14 !important
    border-top-width: 4px !important
  }
</style>
