<template>
  <q-layout ref="layout" view="hHr LpR lFf" :right-breakpoint="1100">
    <q-fixed-position corner="bottom-right" :offset="[18, 96]">
      <q-fab
        color="purple"
        icon="settings"
        direction="up"
        class="vertical-middle"
        id="functions-button"
      >
        <q-fab-action color="secondary" :icon="this.list_state === 'edit'?'close':'mode edit'" id="edit-order-button"
                      @click="on_mode_button_click"/>
        <q-fab-action color="negative" :icon="this.list_state === 'delete'?'close':'delete forever'"
                      @click="on_delete_button_click" id="delete-button"/>
        <q-fab-action color="positive" icon="add" @click="create_new_item" id="new-item-button"/>
      </q-fab>
    </q-fixed-position>
    <q-list class="tasks">
      <draggable v-model="todoList" :options="{group: 'test',animation:'200',handle:'.drag-handle'}" :class="dragging"
                 @start="dragStart" @end="dragEnd">
        <transition-group>
          <q-item v-for="element in todoList" :key="element.id" class="task">
            <q-item-main>
              {{element.name}}
            </q-item-main>
            <q-item-side right>
              <q-item-tile class="drag-handle" v-if="list_state === 'edit'" icon="reorder" color="gray"/>
              <q-item-tile class="delete-item" v-else-if="list_state === 'delete'" icon="remove circle" color="red"
                           @click="remove_item(element.id)"/>
            </q-item-side>
          </q-item>
        </transition-group>
      </draggable>
    </q-list>
  </q-layout>

</template>

<style scoped lang="stylus">
  .sortable-ghost {
    background: #e6e6ff
    color: gray
  }

  .sortable-drag {
    background: white
  }

  .drag-handle:hover {
    cursor: move
  }

  .delete-button {
    cursor: pointer
  }

  .q-list {
    padding: 0
  }

  .q-item:first-of-type {
    border: 3px solid cornflowerblue
    border-right-width: 8px
    border-left-width: 8px
    & .q-item-main {
      position: relative
      left: -8px
    }
    & .q-item-side {
      position: relative
      left: 8px
    }
    transition: border 0.5s
  }

  .test:not(:last-of-type,:first-of-type) {
    border-bottom: solid #bebebe 1px
  }

  .dragging .q-item:first-of-type {
    border: 3px solid white
    border-bottom: solid #bebebe 1px
    border-right-width: 8px
    border-left-width: 8px
  }
</style>

<script>
  import {
    QLayout,
    QList,
    QItem,
    QItemMain,
    QItemSide,
    QItemTile,
    QFab,
    QFabAction,
    QFixedPosition,
    LocalStorage,
    Dialog
  } from 'quasar'
  import draggable from 'vuedraggable'

  export default {
    name: 'ItemList',
    data () {
      return {
        todoList: [],
        list_state: '',
        dragging: '',
        now_id: 0
      }
    },
    methods: {
      save: function () {
        LocalStorage.set('arr', this.todoList)
        LocalStorage.set('now_id', this.now_id)
      },
      create_new_item: function () {
        Dialog.create({
          title: '新的项目',
          message: '创建新项目',
          form: {
            name: {
              type: 'text',
              label: '项目名称',
              model: ''
            }
          },
          buttons: [
            '取消',
            {
              label: '创建',
              handler: (data) => {
                this.todoList.push({'name': data.name, 'id': this.now_id})
                ++this.now_id
                this.save()
              }
            }
          ]
        })
      },
      on_mode_button_click: function () {
        if (this.list_state === 'edit') {
          this.list_state = ''
        }
        else {
          this.list_state = 'edit'
        }
      },
      on_delete_button_click: function () {
        if (this.list_state === 'delete') {
          this.list_state = ''
        }
        else {
          this.list_state = 'delete'
        }
      },
      remove_item: function (id) {
        this.todoList = this.todoList.filter(ele => ele.id !== id)
        this.save()
      },
      dragStart: function () {
        this.dragging = 'dragging'
      },
      dragEnd: function () {
        this.dragging = ''
        this.save()
      }
    },
    components: {
      QLayout,
      draggable,
      QList,
      QItem,
      QItemMain,
      QItemSide,
      QItemTile,
      QFab,
      QFabAction,
      QFixedPosition
    },
    created: function () {
      if (LocalStorage.has('arr')) {
        this.todoList = LocalStorage.get.item('arr')
      }
      if (LocalStorage.has('now_id')) {
        this.now_id = LocalStorage.get.item('now_id')
      }
    }
  }
</script>
