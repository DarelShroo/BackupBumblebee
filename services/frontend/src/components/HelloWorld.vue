<template>
  <div>
    <h1>WebSocket Chat</h1>
    <form @submit.prevent="sendMessage">
      Your ID: <input type="text" v-model="wsId" /><br />
      Message: <input type="text" id="messageText" v-model="message" autocomplete="off"/>
      <button type="submit">Send</button>
    </form>
    <ul id="messages">
      <li v-for="(message, index) in messages" :key="index">{{ message }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld', 
  data() {
    return {
      message: '',
      messages: [],
      wsId: '', 
      ws: null
    };
  },
  methods: {
    sendMessage() {
      if (this.message.trim() !== '' && this.ws) {
        this.ws.send(this.message);
        this.message = '';
      }
    },
    setupWebSocket() {
      if (typeof this.wsId === 'string' && this.wsId.trim() !== '') {
        if (this.wsId.trim() !== '') {
          const wsUrl = `wss://192.168.1.142:8000/wss/${this.wsId}`;
          this.ws = new WebSocket(wsUrl);
          this.ws.onopen = () => {
            console.log('WebSocket connection established.');
          };
          this.ws.onmessage = (event) => {
            this.messages.push(event.data);
          };
          this.ws.onerror = (error) => {
            console.error('WebSocket error:', error);
          };
          this.ws.onclose = () => {
            console.log('WebSocket connection closed.');
          };
        }
    }
    }
  },
  mounted() {
    this.setupWebSocket();
  },
  beforeUnmount() {
    if (this.ws) {
      this.ws.close();
    }
  },
  watch: {
    wsId() {
      if (this.ws) {
        this.ws.close();
      }
      this.setupWebSocket();
    }
  }
};
</script>

<style scoped>
/* Estilos específicos del componente */
</style>
