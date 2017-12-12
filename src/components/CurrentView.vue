<template>
  <div class="major-view">
    <q-card>
      <q-card-title>
        你现在应该做的事是
      </q-card-title>
      <q-card-separator/>
      <q-card-main>
        <q-field
          icon="assignment"
          class="items-center"
        >
          <div id="now-should-do" class="todo-now bg-amber text-white row items-center justify-center">
            <p>{{ todoList.length > 0 ? todoList[0].name : '还没有要做的事……' }}</p>
          </div>
        </q-field>
        <q-btn id="task-finish" @click="on_task_finish">
          <q-icon name="done"/>
          我做完了！
          <q-icon name="mood"/>
        </q-btn>
        <br/>
      </q-card-main>
    </q-card>
  </div>

</template>

<style scoped>

</style>

<script>
  import {
    QCard,
    QCardTitle,
    QCardSeparator,
    QCardMain,
    QField,
    QInput,
    QBtn,
    QIcon,
    LocalStorage
  } from 'quasar'

  export default {
    name: 'CurrentView',
    data () {
      return {
        todoList: []
      }
    },
    components: {
      QCard,
      QCardTitle,
      QCardSeparator,
      QCardMain,
      QField,
      QInput,
      QBtn,
      QIcon
    },
    methods: {
      on_task_finish: function () {
        this.todoList.shift()
        LocalStorage.set('arr', this.todoList)
      }
    },
    mounted: function () {
      if (LocalStorage.has('arr')) {
        this.todoList = LocalStorage.get.item('arr')
      }
    }
  }
</script>
