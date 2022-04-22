module.exports = {
  mode : "JIT",
  purge : ["../views/*.html"],
  content: [],
  theme: {
    extend: {
      colors:{
        "blue1": "#1DA1F2",
        "blue2": "#2795D9",
        "blue": "#EFF9FF",
        "dark": "#657786",
        "light": "#AAB8C2",
        "lighter": "#E1E8ED",
        "lightest": "#F5F8FA",
        "lightgrey": "#71767b",
        "mediumgrey": "#202327",
        "darkgrey": "#16181c"
      },
      backgroundImage: {
        "twitter-bg": "url('/images/twitter_bg.png')"
      },
      fontFamily: {
        "main-heading": ["Work Sans", "sans-serif"]
      },
      fontSize: {
        "100xl": "30rem"
      }         
    },
  },
  plugins: [],
}
