import React, { useState } from "react";

const Cam = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
      <img
        src="http://localhost:8080/video_feed"
        alt="Video"
      />
    </div>
  );
};
export default Cam;