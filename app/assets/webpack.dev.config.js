var webpack = require('webpack')
var config = require('./webpack.config.js');

config.mode = "development";

config.devServer = {
    disableHostCheck: true,
    noInfo: false,
    host: '0.0.0.0',
    port: 8080,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
      "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
   }
};

config.output.publicPath = 'http://0.0.0.0:8080/static/bundles/';
config.plugins.push(new webpack.DefinePlugin({
    'process.env':{
        'NODE_ENV': JSON.stringify('development')
    }
}));

module.exports = config;
