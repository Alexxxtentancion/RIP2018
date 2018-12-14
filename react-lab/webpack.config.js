const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
    entry: './src/index.js',
    module: {
        rules: [
          {
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: ['babel-loader']
          },
          {
              test: /\.(png|jpg|gif)$/,
              use:[
                  {
                      loader: "file-loader",
                    options:{
                        name:'static/img/[name].[ext]'
                    }}]
          },
          {
              test: /\.css$/,
              use: [
                  
                      {loader:"style-loader"},
                      {loader:"css-loader"}
                  
              ]
          }
        ]
      },
      resolve: {
        extensions: ['*', '.js', '.jsx']
      },
    output: {
      path: __dirname + './dist',
      publicPath: '/',
      filename: 'bundle.js'
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new HtmlWebpackPlugin({template: './dist/index.html'})
      ],
    devServer: {
      contentBase: './dist'
    }
  };