import React from 'react';
import HomeScreen from './Screens/HomeScreen/HomeScreen';
import GenerateScreen from './Screens/GenerateScreen/GenerateScreen';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
            <Route path="/"
              element={<HomeScreen />}>
            </Route>
            <Route path="/notes"
              element={<GenerateScreen />}>
            </Route>
          </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;