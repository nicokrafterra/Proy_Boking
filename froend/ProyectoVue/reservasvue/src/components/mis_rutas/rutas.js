import { createRouter, createWebHistory } from "vue-router";
import Perfil from "../Perfil.vue";
import Reserva from "../Reserva.vue";
import Platos from "../Platos.vue";
import Pricipal from "../Pricipal.vue";
import Formu from "../Formu.vue";

const routes = [
    {
        path: "/index",
        name: "index",
        component:Pricipal
    },
    {
        path: "/Perfil",
        name: "Perfil",
        component: Perfil
    },
    {
        path: "/Reservas",
        name: "Reservas",
        component: Reserva
    },
    {
        path: "/Platos",
        name: "Platos",
        component: Platos
    },
    {
        path: "/Login",
        name: "Login",
        component: Formu
    }


];
const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router