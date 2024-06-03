<template>
    <div>
      <!-- Hero Section -->
      <section class="hero d-flex align-items-center animate__animated animate__fadeIn">
        <div class="container">
          <div class="row">
            <div class="col-lg-6">
              <br><br><br><br><br><br>
              <h1>Welcome to </h1>
              <h1>Y & S Finance Service</h1>
              <p class="mt-4">Discover secure and reliable financial services tailored to your needs.</p>
            </div>
            <div class="col-lg-6 d-flex justify-content-center">
              <!-- <img src="@/assets/result_rich2.png" class="img-fluid" alt="Welcome Image"> -->
            </div>
          </div>
        </div>
      </section>
  
      <!-- Cards -->
    <div class="container mt-5 mb-5">
      <div class="row">
        <div class="col-md-4 mb-4 animate__animated animate__zoomIn">
          <div class="card">
            <img src="@/assets/busy.jpg" class="card-img-top" alt="Online Banking">
            <div class="card-body">
              <h2 class="card-title">Deposit Products</h2>
              <p class="card-text">Come here and look around our products!</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4 animate__animated animate__zoomIn" style="animation-delay: 0.2s;">
          <div class="card">
            <img src="@/assets/bank2.jpg" class="card-img-top" alt="Loans">
            <div class="card-body">
              <h5 class="card-title">Recommend Products</h5>
              <p class="card-text">Find the perfect financial product for me!</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4 animate__animated animate__zoomIn" style="animation-delay: 0.4s;">
          <div class="card">
            <img src="@/assets/people.jpg" class="card-img-top" alt="Support">
            <div class="card-body">
              <h5 class="card-title">Y&S Community Board</h5>
              <p class="card-text">Check out    information and feel free to communicate!</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </template>
  
  <script setup>
  import 'animate.css';
  </script>
  
  <style scoped>
  .hero {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('@/assets/newyork.jpg') center center/cover no-repeat;
    height: 50vh;
  }
  
  .hero h1 {
    color: #fff;
    font-size: 3rem;
  }
  
  .hero p {
    color: #fff;
  }
  
  .btn-primary {
    background-color: #007bff;
    border-color: #007bff;
  }
  
  .btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
  }
  
  .services {
    padding: 80px 0;
  }
  
  .service-item {
    text-align: center;
    padding: 30px;
    background-color: #f8f9fa;
    border-radius: 10px;
    transition: transform 0.3s ease-in-out;
  }
  
  .service-item:hover {
    transform: translateY(-10px);
  }
  
  .service-item i {
    font-size: 3rem;
    color: #007bff;
  }
  
  .service-item h3 {
    font-size: 1.5rem;
    margin-top: 20px;
  }
  
  .service-item p {
    font-size: 1rem;
    color: #6c757d;
  }
  </style>
  
  