const path = require('path');

module.exports = {
  entry: './public/startup.js',
  mode: 'development', // o 'production'
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};

