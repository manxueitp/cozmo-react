/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View
} from 'react-native';
import SocketIOClient from 'socket.io-client';

export default class CozmoProject extends Component {
  constructor(props) {
    super(props);
    // Creating the socket-client instance will automatically connect to the server.
    this.socket = SocketIOClient('http://localhost:3000');
  }
}

AppRegistry.registerComponent('CozmoProject', () => CozmoProject);
