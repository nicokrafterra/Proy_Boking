<template>
    <header>
      <div class="A-logo">
        <svg width="1103" height="996" viewBox="0 0 1103 996" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M410.988 255.56L0 995.337H189.802L505.141 427.427L410.988 255.56ZM1102.94 995.337L647.119 170.373L551.471 0L457.317 170.373L551.471 340.746L711.79 629.718H498.683L405.461 786.972H799.034L914.634 995.337H1102.94Z" fill="#FAFBFC"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M410.988 255.56L0 995.337H189.802L505.141 427.427L410.988 255.56ZM1102.94 995.337L647.119 170.373L551.471 0L457.317 170.373L551.471 340.746L711.79 629.718H498.683L405.461 786.972H799.034L914.634 995.337H1102.94Z" fill="#FAFBFC"/>
        </svg>
      </div>
      <span class="navegar__Usuario">
        <img class="icon" src="../assets/IMG/message.svg" alt="Mensaje" />
        <img class="icon" src="../assets/IMG/notification.svg" alt="Notificacion" />
        <img class="perfil" src="../assets/IMG/foto.png" alt="Usuario-perfil" @click="toggleDropdown" />
      </span>
      <div 
        class="Menu-desple" 
        :class="{ hide: isHidden, 'Menu-desple-gable': isFading }"
        ref="Menu"
      >
        <div class="Menu__group">
          <div class="nombre-usuario">Guillermo Vargas</div>
          <div class="email">ASTROWORDL@gmail.com</div>
        </div>
        <hr class="divider" />
        <nav>
          <ul>
          <router-link class="ramdon"to="/Perfil"><img src="../assets/IMG/profile.svg" alt="Perfil" /> Mi Perfil</router-link>

            <li><img src="..//assets/IMG/settings.svg" alt="Ajustes" />Ajustes</li>
          </ul>
          <hr class="divider" />
          <ul>
					<router-link class="ramdon" to="/Reservas" ><img src="../assets/IMG/tutorials.svg" alt="Reservas" />Mis reservas</router-link>
          </ul>
          <hr class="divider" />
          <ul>
            <li style="color: #E3452F;"><img src="../assets/IMG/logout.svg" alt="Log Out" /> Salir</li>
          </ul>
        </nav>
      </div>
    </header>
</template>
<script setup>

</script>

<style>
  header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 80px;
  padding: 0 16px;
  width: 100%;
  display: flex;
  align-items: center;
  background-color: var(--primary);
  justify-content: end;
  z-index: 1000;
}
</style>