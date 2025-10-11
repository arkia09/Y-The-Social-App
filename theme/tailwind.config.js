/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../templates/base.html",
    // "./templates/**/*.html",
    // "./static_src/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["DM Sans", "sans-serif"],
      },
      colors: {
        card: "#ffffff",
        accent: {
          blue: "#A5D8FF",
          lavender: "#D0BFFF",
          mint: "#BFFFC8",
        },
        text: "#1a1a1a",
      },
      boxShadow: {
        soft: "0 2px 10px rgba(0,0,0,0.05)",
      },
    },
  },
  plugins: [],
};
