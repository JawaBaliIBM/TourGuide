module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: [
      {
        mytheme: {
          primary: '#33C072',
          secondary: '#00A5CF',
          accent: '#F3680C',
          neutral: '#33C072',
          'base-100': '#FFFFFF',
          info: '#CAE2E8',
          success: '#DFF2A1',
          warning: '#F7E488',
          error: '#F2B6B5',
        },
      },
    ],
  },
  plugins: [require('@tailwindcss/typography'), require('daisyui')],
};
