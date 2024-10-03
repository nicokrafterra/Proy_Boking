<template>
	<div class="reserva-form">
	  <h2>Formulario de Reserva</h2>
	  <form @submit.prevent="hacerReserva">
		<div class="form-group">
		  <label for="usuario_id">ID de Usuario:</label>
		  <input type="number" id="usuario_id" v-model="usuario_id" required />
		</div>
  
		<div class="form-group">
		  <label for="fecha">Fecha de Reserva:</label>
		  <input type="date" id="fecha" v-model="fecha" required />
		</div>
  
		<div class="form-group">
		  <label for="tipo_Reserva">Tipo de Reserva:</label>
		  <input type="text" id="tipo_Reserva" v-model="tipo_Reserva" required />
		</div>
  
		<button type="submit">Hacer Reserva</button>
	  </form>
	</div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const usuario_id = ref('');
  const fecha = ref('');
  const tipo_Reserva = ref('');
  
  const hacerReserva = async () => {
	const reservaData = {
	  usuario_id: parseInt(usuario_id.value), // Convertir a número entero
	  fecha: fecha.value,
	  tipo_Reserva: tipo_Reserva.value,
	};
  
	try {
	  const response = await fetch('http://localhost:8000/reservas/', {
		method: 'POST',
		headers: {
		  'Content-Type': 'application/json',
		},
		body: JSON.stringify(reservaData),
	  });
  
	  if (!response.ok) {
		throw new Error('Error al hacer la reserva');
	  }
  
	  const data = await response.json();
	  console.log('Reserva exitosa:', data);
  
	  // Resetear el formulario después de la reserva
	  usuario_id.value = '';
	  fecha.value = '';
	  tipo_Reserva.value = '';
	} catch (error) {
	  console.error('Error:', error);
	  alert('No se pudo realizar la reserva. Intenta nuevamente.');
	}
  };
  </script>
  
  <style scoped>
  .reserva-form {
	max-width: 400px;
	margin: auto;
	padding: 20px;
	border: 2px solid #4caf50; /* Verde */
	border-radius: 10px;
	background-color: #f9f9f9;
	box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  h2 {
	color: #ff9800; /* Naranja */
	text-align: center;
  }
  
  .form-group {
	margin-bottom: 15px;
  }
  
  label {
	display: block;
	margin-bottom: 5px;
	font-weight: bold;
	color: #333;
  }
  
  input {
	width: 100%;
	padding: 10px;
	border: 2px solid #4caf50; /* Verde */
	border-radius: 5px;
	box-sizing: border-box;
	transition: border-color 0.3s;
  }
  
  input:focus {
	border-color: #ff9800; /* Naranja */
	outline: none;
  }
  
  button {
	padding: 10px 15px;
	background-color: #4caf50; /* Verde */
	color: white;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	font-weight: bold;
	transition: background-color 0.3s;
  }
  
  button:hover {
	background-color: #ff9800; /* Naranja */
  }
  </style>
  