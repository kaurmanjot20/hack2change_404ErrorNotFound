import React, { useEffect } from 'react';
import { FaCalendar, FaChartLine, FaCogs, FaCloudSun, FaWater, FaLeaf } from 'react-icons/fa';
import missionImage from '../assets/pic5.png';
import aboutUsImageRight from '../assets/pic4.png'; // New image import

function Home() {
  useEffect(() => {
    const cards = document.querySelectorAll('.card');

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate');
            observer.unobserve(entry.target); // Stop observing after animation
          }
        });
      },
      { threshold: 0.1 } // Adjust this value as needed
    );

    cards.forEach((card) => {
      observer.observe(card);
    });
  }, []);

  return (
    <div className="home">
      <section className="about-us">
        <div className="about-text">
          <h2>Welcome to AgroSphere!</h2>
          <p>
            At AgroSphere, we understand the unique challenges faced by modern farmers.
            With the ever-changing climate and evolving agricultural practices, we are
            here to provide you with a comprehensive solution that empowers you to thrive
            in today's dynamic farming environment.
          </p>
        </div>
        <img src={aboutUsImageRight} alt="About Us" />
      </section>

      <section className="mission">
        <img src={missionImage} alt="Our Mission" />
        <div className="mission-text">
          <h2>Our Mission</h2>
          <p>
            Our mission is to revolutionize farming practices by leveraging cutting-edge
            technology. We combine the power of Artificial Intelligence (AI), Machine
            Learning (ML), and the Internet of Things (IoT) to offer you an intuitive,
            data-driven dashboard designed to enhance your farming experience. Our goal
            is to help you make informed decisions, optimize resource allocation, and
            ultimately, increase your crop yields.
          </p>
        </div>
      </section>

      <section className="what-we-offer">
        <h2>What We Offer</h2>
        <div className="cards">
          <div className="card">
            <FaCalendar className="card-icon" />
            <h3>Optimized Planting Schedules</h3>
            <p>
              Receive tailored recommendations for the best times to plant based on historical
              climate data and real-time weather forecasts.
            </p>
          </div>
          <div className="card">
            <FaChartLine className="card-icon" />
            <h3>Resource Allocation Insights</h3>
            <p>
              Efficiently manage your resources with data-driven insights, ensuring optimal use
              of water, nutrients, and other essential inputs.
            </p>
          </div>
          <div className="card">
            <FaCogs className="card-icon" />
            <h3>Yield Prediction</h3>
            <p>
              Utilize advanced machine learning models to forecast your crop yields and plan
              accordingly.
            </p>
          </div>
          <div className="card">
            <FaCloudSun className="card-icon" />
            <h3>Real-Time Farm Monitoring</h3>
            <p>
              Stay informed with real-time data on soil moisture, temperature, and light levels,
              all captured through our state-of-the-art sensor network.
            </p>
          </div>
          <div className="card">
            <FaWater className="card-icon" />
            <h3>Automated Irrigation Management</h3>
            <p>
              Reduce water wastage with automated irrigation systems that adapt to your crops'
              needs and current soil conditions.
            </p>
          </div>
          <div className="card">
            <FaLeaf className="card-icon" />
            <h3>Soil Health Analysis</h3>
            <p>
              Get detailed insights into soil health to make informed decisions about nutrient
              management and soil care.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;
