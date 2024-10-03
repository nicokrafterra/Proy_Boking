<script setup>
</script>

<template>
	<div id="Container-Perfil">
		<div id="Container-Foto">
			<img id="Foto-Perfil" src="../assets/IMG/foto.png" alt="">
		</div>
		<h1>Guillermo avila</h1>
		<p>Rol: administrador</p>
		<p>correo: ASTROWORDL@gmail.com</p>
	</div>
</template>

<script setup>
</script>

<style>
#Container-Perfil {
  background-color: #f5f5f5;
  border-radius: 10px;
  padding: 20px;
  max-width: 350px;
  margin: 0 auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-family: 'Arial', sans-serif;
}

#Container-Foto {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 15px;
}

#Foto-Perfil {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 3px solid #4CAF50;
  object-fit: cover;
}

h1 {
  font-size: 24px;
  color: #333;
  margin-bottom: 5px;
}

p {
  font-size: 16px;
  color: #666;
  margin: 5px 0;
}

p:first-of-type {
  font-weight: bold;
}

p:last-of-type {
  font-style: italic;
  color: #888;
  text-transform: lowercase;
}
</style>