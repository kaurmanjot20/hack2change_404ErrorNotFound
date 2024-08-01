import React, { useState } from 'react';
import axios from 'axios';

export default function CropPrediction() {
  const [formData, setFormData] = useState({
    State_Name: '',
    Crop_Type: '',
    Crop: '',
    N: '',
    P: '',
    K: '',
    ph: '',
    rainfall: '',
    temperature: '',
    Area_in_hectares: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/ml_model/predict/', formData);
      console.log(response.data);
      // Handle the response data as needed (e.g., display prediction results)
    } catch (error) {
      console.error('Error submitting form:', error);
      // Handle errors (e.g., display error message to user)
    }
  };

  return (
    <div className="crop-prediction">
      <h2>Crop Prediction</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="State_Name">State:</label>
          <input
            type="text"
            id="State_Name"
            name="State_Name"
            value={formData.State_Name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="Crop_Type">Crop Type:</label>
          <input
            type="text"
            id="Crop_Type"
            name="Crop_Type"
            value={formData.Crop_Type}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="Crop">Crop:</label>
          <input
            type="text"
            id="Crop"
            name="Crop"
            value={formData.Crop}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="N">Nitrogen:</label>
          <input
            type="number"
            id="N"
            name="N"
            value={formData.N}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="P">Phosphorus:</label>
          <input
            type="number"
            id="P"
            name="P"
            value={formData.P}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="K">Potassium:</label>
          <input
            type="number"
            id="K"
            name="K"
            value={formData.K}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="pH">pH:</label>
          <input
            type="number"
            id="pH"
            name="pH"
            value={formData.pH}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="rainfall">Rainfall:</label>
          <input
            type="number"
            id="rainfall"
            name="rainfall"
            value={formData.rainfall}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="temperature">Temperature:</label>
          <input
            type="number"
            id="temperature"
            name="temperature"
            value={formData.temperature}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="Area_in_hectares">Area in hectares:</label>
          <input
            type="number"
            id="Area_in_hectares"
            name="Area_in_hectares"
            value={formData.Area_in_hectares}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}