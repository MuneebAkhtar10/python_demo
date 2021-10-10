import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render(props) {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Generate four types of printable random objects</h1>
        </header>
        <p className="App-intro">
          <p> {props.filesize} </p>
        </p>
      </div>
    );
  }
}

export default App;
