
import React from "react";
import { Nav, NavLink, NavMenu }
  from "./NavbarElements.js";


const Navigation = () => {
  return (
    <>
      <Nav>
        <NavMenu>
          <NavLink to="/about" activeStyle>
            Home
          </NavLink>
          <NavLink to="/ASL" activeStyle>
            ASL to English
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};

export default Navigation;