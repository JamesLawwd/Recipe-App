import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css';
import React from 'react';
import { createRoot } from 'react-dom/client'; // Import createRoot from react-dom

import NavBar from './components/Navbar';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/Home';
import SignUpPage from './components/SignUp';
import LoginPage from './components/Login';
import CreateRecipePage from './components/CreateRecipe';

const App = () => {
    return (
        <Router>
            <div className="">
                <NavBar />
                <Routes>
                    <Route path="/create_recipe" element={<CreateRecipePage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/signup" element={<SignUpPage />} />
                    <Route path="/" element={<HomePage />} />
                </Routes>
            </div>
        </Router>
    );
};

// Use createRoot to render your application
const root = createRoot(document.getElementById('root'));
root.render(<App />);
