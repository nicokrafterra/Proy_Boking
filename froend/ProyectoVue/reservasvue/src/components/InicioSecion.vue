<script setup>
import { ref } from 'vue';

const email = ref('');
const password = ref('');
const emailError = ref('');
const passwordError = ref('');

const iniciarSesion = (event) => {
  event.preventDefault();
  clearErrors();
  let valid = true;

  if (!email.value) {
    emailError.value = 'El correo electrónico es obligatorio.';
    valid = false;
  } else if (!validEmail(email.value)) {
    emailError.value = 'Por favor, introduce un correo electrónico válido.';
    valid = false;
  }

  if (!password.value) {
    passwordError.value = 'La contraseña es obligatoria.';
    valid = false;
  }

  if (valid) {
    alert('Inicio de sesión exitoso!');
    router.push('/index');
  }
};

const validEmail = (email) => {
  const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return emailPattern.test(email);
};

const clearErrors = () => {
  emailError.value = '';
  passwordError.value = '';
};
</script>

<template>
  <div id="cajaInicioSesion">
    <form id="Formu">
      <div id="Cajas">
        <label for="email">Usuario/Correo</label>
        <input
          type="text"
          id="email"
          class="CajasForm"
          placeholder="Ingresa tu correo"
          v-model="email"
        />
        <div v-if="emailError" style="color: red">{{ emailError }}</div>
      </div>
      <div id="Cajas">
        <label for="password">Contraseña</label>
        <input
          type="password"
          id="password"
          class="CajasForm"
          placeholder="Ingresa tu contraseña"
          v-model="password"
        />
        <div v-if="passwordError" style="color: red">{{ passwordError }}</div>
      </div>
      <p>¿No tienes una Cuenta? <a href="#" @click.prevent="$emit('show-registro')">Registrarse</a></p>
      <button @click="iniciarSesion">Iniciar Sesión</button>
    </form>
  </div>
</template>

<style>
#cajaInicioSesion {
  background-color: #f0f0f0;
  height: auto;
  width: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

#Formu {
  width: 80%;
}

#Cajas {
  margin-bottom: 20px;
}

.CajasForm {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}
</style>
