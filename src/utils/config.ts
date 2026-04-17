import dotenv from 'dotenv';

dotenv.config();

export const config = {
  baseUrl: (process.env.BASE_URL || 'https://angular-qa-recruitment-app.netlify.app').replace(/\/$/, ''),
  formUrl: '/form',
  stepperUrl: '/stepper',
  stepperAdvancedUrl: '/stepper-advanced',
  welcomeUrl: '/',
  
  // Timeouts (in milliseconds)
  defaultTimeout: 5000,
  navigationTimeout: 10000,
  elementWaitTimeout: 3000,

  // Test data
  testUser: {
    name: 'John Doe',
    alterEgo: 'Superman',
    heroPower: 'Flying',
  },
  testUserStep: {
    name: 'Jane Smith',
    address: '123 Main St, Anytown, USA',
  },
};

export default config;
