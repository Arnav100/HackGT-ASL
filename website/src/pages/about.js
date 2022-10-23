import React from "react";
import "./about.css";
import ASLToEnglish from "../components/ASL";
import { useRef } from 'react';
import { Button } from 'react-bootstrap';
import Cam from "../components/Cam";

const Home = () => {
  const ref = useRef(null);
  const handleClick = () => {
    ref.current?.scrollIntoView({ block: "start", inline: "nearest", behavior: 'smooth' });
  };
  return (
    <>
      <div id="background-img">
      </div>
      <div id="text-area">
        <h1 className="headertext">
          Welcome to Big Red ASL!
        </h1>
        <p>
          Our project provides live ASL to English and English to ASL translation!
        </p>
        <style type="text/css">
          {`
    .btn-flat {
      background-color: white;
      color: black;
      font-weight: bold;
    }
    .btn-flat:hover {
      background-color:#b31b1b;
      color: white;
    }
    .btn-xxl {
      padding: 1rem 1.5rem;
      font-size: 1.5rem;
    }
    `}
        </style>
        <Button variant="flat" size="xxl" onClick={handleClick}>"Start Translating!"</Button>
      </div>
      <div ref={ref}>
        <ASLToEnglish id="ASLToEnglish" />
      </div>
      <Cam/>
      <div style = {{height: "155rem"}}/>
    </>
  );
};

export default Home;