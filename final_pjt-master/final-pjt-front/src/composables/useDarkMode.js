import { ref, provide, inject } from 'vue';

const darkModeSymbol = Symbol();

export function provideDarkMode() {
  const isDarkMode = ref(false);

  const toggleDarkMode = () => {
    isDarkMode.value = !isDarkMode.value;
    if (isDarkMode.value) {
      document.documentElement.classList.add('dark-mode');
    } else {
      document.documentElement.classList.remove('dark-mode');
    }
  };

  provide(darkModeSymbol, {
    isDarkMode,
    toggleDarkMode
  });
}

export function useDarkMode() {
  const darkMode = inject(darkModeSymbol);
  if (!darkMode) {
    throw new Error('useDarkMode must be used within a provideDarkMode context');
  }
  return darkMode;
}
