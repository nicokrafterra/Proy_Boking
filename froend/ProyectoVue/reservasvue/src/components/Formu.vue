<template>
	<div class="login-page">
		<div class="form">
			<!-- Registro de Usuario -->
			<form v-if="isRegistering" class="register-form" @submit.prevent="handleRegister">
				<h2><i class="fas fa-lock"></i> Register</h2>
				<input type="text" v-model="nombre" placeholder="Nombre *" required />
				<div v-if="nombreError" style="color: red">{{ nombreError }}</div>

				<input type="text" v-model="apellido" placeholder="Apellido *" required />
				<div v-if="apellidoError" style="color: red">{{ apellidoError }}</div>

				<input type="email" v-model="email" placeholder="Email *" required />
				<div v-if="emailError" style="color: red">{{ emailError }}</div>

				<input type="password" v-model="password" placeholder="Password *" required />
				<div v-if="passwordError" style="color: red">{{ passwordError }}</div>

				<input type="password" v-model="vpassword" placeholder="Confirmar Password *" required />
				<div v-if="vpasswordError" style="color: red">{{ vpasswordError }}</div>

				<input type="number" v-model="edad" placeholder="Edad *" required />
				<div v-if="edadError" style="color: red">{{ edadError }}</div>

				<input type="text" v-model="numeroCelular" placeholder="Número de Celular *" required />
				<div v-if="celularError" style="color: red">{{ celularError }}</div>

				<button type="submit">Create</button>
				<p class="message">Already registered? <a href="#" @click.prevent="toggleForm">Sign In</a></p>
			</form>

			<!-- Inicio de Sesión -->
			<form v-else class="login-form" @submit.prevent="handleLogin">
				<h2><i class="fas fa-lock"></i> Login</h2>
				<input type="text" v-model="username" placeholder="Username" required />
				<div v-if="loginError" style="color: red">{{ loginError }}</div>

				<input type="password" v-model="password" placeholder="Password" required />
				<div v-if="loginPasswordError" style="color: red">{{ loginPasswordError }}</div>

				<button type="submit">Login</button>
				<p class="message">Not registered? <a href="#" @click.prevent="toggleForm">Create an account</a></p>
			</form>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
	data() {
		return {
			isRegistering: true,
			nombre: '',
			apellido: '',
			email: '',
			password: '',
			vpassword: '',
			edad: null,
			numeroCelular: '',
			username: '',
			loginError: '',
			loginPasswordError: '',
			nombreError: '',
			apellidoError: '',
			emailError: '',
			passwordError: '',
			vpasswordError: '',
			edadError: '',
			celularError: ''
		};
	},
	methods: {
		toggleForm() {
			this.isRegistering = !this.isRegistering;
			this.clearErrors();
		},
		clearErrors() {
			this.nombreError = '';
			this.apellidoError = '';
			this.emailError = '';
			this.passwordError = '';
			this.vpasswordError = '';
			this.edadError = '';
			this.celularError = '';
			this.loginError = '';
			this.loginPasswordError = '';
		},
		async handleRegister() {
  this.clearErrors();
  let valid = true;

  // Validación del nombre (solo letras)
  const nombreRegex = /^[a-zA-Z\s]+$/;
  if (!this.nombre) {
    this.nombreError = 'El nombre es obligatorio.';
    valid = false;
  } else if (!nombreRegex.test(this.nombre)) {
    this.nombreError = 'El nombre solo debe contener letras.';
    valid = false;
  }

  // Validación del apellido (solo letras)
  if (!this.apellido) {
    this.apellidoError = 'El apellido es obligatorio.';
    valid = false;
  } else if (!nombreRegex.test(this.apellido)) {
    this.apellidoError = 'El apellido solo debe contener letras.';
    valid = false;
  }

  // Validación del correo electrónico
  if (!this.email) {
    this.emailError = 'El correo electrónico es obligatorio.';
    valid = false;
  } else if (!this.validEmail(this.email)) {
    this.emailError = 'Por favor, introduce un correo electrónico válido.';
    valid = false;
  }

  // Validación de la contraseña
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d{3,})(?=.*[!@#$%^&*_-])[A-Za-z\d!@#$%^&*_-]{8,}$/;
  if (!this.password) {
    this.passwordError = 'La contraseña es obligatoria.';
    valid = false;
  } else if (!passwordRegex.test(this.password)) {
    this.passwordError = 'La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula, 3 números y un carácter especial.';
    valid = false;
  }

  // Confirmar contraseñas
  if (this.password !== this.vpassword) {
    this.vpasswordError = 'Las contraseñas no coinciden.';
    valid = false;
  }

  // Validación de la edad
  if (this.edad === null || this.edad <= 0) {
    this.edadError = 'Por favor, introduce una edad válida.';
    valid = false;
  }

  // Validación del número de celular (mínimo 10 dígitos)
  if (!this.numeroCelular || this.numeroCelular.length < 10) {
    this.celularError = 'Por favor, introduce un número de celular válido (mínimo 10 dígitos).';
    valid = false;
  }

  if (valid) {
    try {
      const response = await axios.post('http://localhost:8000/usuarios/', {
        nombre: this.nombre,
        apellido: this.apellido,
        correoElectronico: this.email,
        contraseñaUsuario: this.password,
        numeroCelular: this.numeroCelular,
        edad: this.edad,
        esAdmin: false
      });
      alert('Registro exitoso!');
      console.log(response.data);
    } catch (error) {
      console.error('Error al registrar el usuario:', error);
      alert('Error al registrar el usuario.');
    }
  }
},
		async handleLogin() {
			this.clearErrors();
			try {
				const response = await axios.post('http://localhost:8000/usuarios/', {
					username: this.username,
					password: this.password
				});
				console.log('Inicio de sesión exitoso:', response.data);
			} catch (error) {
				this.loginError = 'Error al iniciar sesión. Por favor, verifica tus credenciales.';
				console.error('Error en inicio de sesión:', error);
			}
		},
		validEmail(email) {
			const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
			return emailPattern.test(email);
		}
	}
};
</script>


<style scoped>
@import url(https://fonts.googleapis.com/css?family=Poppins:300);

body {
	height: 100vh;
	overflow: hidden;
	font-family: "Poppins";
	background: #0e2941;
}

.login-page {
	width: 400px;
	padding: 8% 0 0;
	margin: auto;
}

.form {
	position: relative;
	z-index: 1;
	background: #FFFFFF;
	max-width: 400px;
	margin: 0 auto 100px;
	padding: 45px;
	text-align: center;
	border-radius: 15px;
	box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}

.form input {
	font-family: "Poppins", sans-serif;
	outline: 0;
	background: #f2f2f2;
	width: 100%;
	border: 0;
	border-radius: 7px;
	margin: 0 0 15px;
	padding: 15px;
	box-sizing: border-box;
	font-size: 14px;
}

.form button {
	font-family: "Poppins", sans-serif;
	text-transform: uppercase;
	outline: 0;
	background: #234666;
	width: 100%;
	border: 0;
	padding: 15px;
	color: #FFFFFF;
	border-radius: 7px;
	font-size: 14px;
	-webkit-transition: all 0.3 ease;
	transition: all 0.3 ease;
	cursor: pointer;
}

.form button:hover,
.form button:active,
.form button:focus {
	background: #0e2941;
}

.form .message {
	margin: 15px 0 0;
	color: #b3b3b3;
	font-size: 12px;
}

.form .message a {
	color: #234666;
	text-decoration: none;
}
</style>