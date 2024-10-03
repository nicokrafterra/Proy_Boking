<script setup>
import { ref } from 'vue';
import Pricipal from './components/Pricipal.vue';
import Reserva from './components/Reserva.vue';
import Perfil from './components/Perfil.vue';
import Platos from './components/Platos.vue';
import Formu from './components/Formu.vue';
import Headerr from './components/Headerr.vue';
</script>

<template>
	
	<Headerr/>
	<Formu/>
	<router-view></router-view>
	
</template>

<style>

</style>
