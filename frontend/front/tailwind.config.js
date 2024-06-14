/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1370px',
      '2xl': '1536px',
    },
    fontFamily: {
      'inter': ['"Inter"', 'Helvetica'],
      'syncopate': ['"Syncopate"', 'Helvetica']
    },
    extend: {},
  },
  plugins: [],
};
