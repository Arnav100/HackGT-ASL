import React from 'react';
import './App.css';
import Navigation from './components/Navbar';
import { BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import Home from './pages/about';
import ASLToEnglish from './components/ASL';
  
function App() {
return (
    <Router>
    {/* <Navigation /> */}
    <Routes>
        <Route path='/about' element={<Home/>} />
        <Route path = '/asl' element = {<ASLToEnglish/>}/>
    </Routes>
    </Router>
);
}
  
export default App;
