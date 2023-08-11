import {writable} from 'svelte/store';

export let isAuthenticated = writable(true);
export let token = writable('');
export let user = writable({});
export let popupOpen = writable(false);
export let error = writable();