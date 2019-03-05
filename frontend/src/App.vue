<template>
  <div id="app">
    <div class="text-xs-center">
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark v-on="on">
            MENU
          </v-btn>
        </template>
        <v-list>
          <v-list-tile v-for="(item, index) in items" :key="index">
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </div>
    <div class="container">
      {{ message }}
    </div>
    <div class="container">
      <div class="row my-5">
        <div class="col">
          <h3>{{ hello_bootstrap }}</h3>
        </div>
        <div class="col">
          <div class="alert alert-secondary" role="alert">
            Интернет-магазин GeekBrains
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'app',
    components: {},
    data() {
      return {
        message: 'HELLO VUE!!!',
        hello_bootstrap: 'We use BOOTSTRAP! and Vuetify!',
        items : [
          {title: 'one'},
          {title: 'two'},
          {title: 'three'},
          {title: 'four'},
          {title: 'five'},
        ]
      }
    }
  }
</script>