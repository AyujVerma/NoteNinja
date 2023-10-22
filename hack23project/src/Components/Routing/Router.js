import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomeScreen from '../../Screens/HomeScreen/HomeScreen.js';
import GenerateScreen from '../../Screens/GenerateScreen/GenerateScreen.js';

const AppRouter = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomeScreen />} />
        <Route path="/generate" element={<GenerateScreen />} />
      </Routes>
    </Router>
  );
};

export default AppRouter;