const path = require('path');

module.exports = {
  entry: './frontend/src/index.js',
  output: {
    path: path.resolve(__dirname, 'frontend/static/frontend/bundles/'),
    filename: 'main.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  }
};
