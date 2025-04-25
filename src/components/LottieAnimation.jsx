import React from 'react';
import Lottie from 'react-lottie';
import animationData from './assets/Animation - 1745580787370.json'; // Adjust path if needed

const LottieAnimation = () => {
  const defaultOptions = {
    loop: true, // Set whether the animation should loop
    autoplay: true, // Start playing immediately
    animationData: animationData, // Your Lottie JSON data
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice" // Controls how the animation scales
    }
  };

  return (
    <div>
      <Lottie options={defaultOptions} height={400} width={400} />
    </div>
  );
};

export default LottieAnimation;
