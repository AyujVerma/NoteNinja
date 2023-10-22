import React from 'react';
import { Routes , Route } from 'react-router-dom';
import HomeScreen from '../../Screens/HomeScreen/HomeScreen.js';
import GenerateScreen from '../../Screens/GenerateScreen/GenerateScreen.js';

function AppRouter() {
  return (
    <div className="App">
      <Routes>
        <Route path='/generate' element={<GenerateScreen/>} />
        <Route path='/' element={<HomeScreen/>} />
      </Routes>
    </div>
  );
}

export default AppRouter;
