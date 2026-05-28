/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        heading: ['"Inter Tight"', 'sans-serif'],
        body:    ['"Inter Tight"', 'sans-serif'],
        sans:    ['"Inter Tight"', 'sans-serif'],
      },
      colors: {
        pageBg: '#F2F2F0',
        primaryText: '#111111',
        brandRed: '#C0392B',
        brandTeal: '#4ECDC4',
        brandBlue: '#4D7EFF',
        brandGreen: '#3DBF7A',
        eyebrow: 'rgba(0,0,0,0.45)',
        bodyCopy: 'rgba(0,0,0,0.55)',
        outlineBorder: 'rgba(0,0,0,0.15)',
        hoverBg: 'rgba(0,0,0,0.05)',
      }
    },
  },
  plugins: [],
}
