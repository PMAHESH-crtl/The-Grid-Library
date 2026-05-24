import React, { useState } from "react";

const qrCodeImage =
  "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=UPI-7995966131-ptsbi";

export default function TheGridLibrary() {
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [showPopup, setShowPopup] = useState(false);
  const [showPaymentModal, setShowPaymentModal] = useState(false);
  const [showReceipt, setShowReceipt] = useState(false);
  const [customerName, setCustomerName] = useState("");
  const [paymentId, setPaymentId] = useState("");

  const products = [
    {
      id: 1,
      name: "Classic Wooden Frame",
      category: "Standard Frames",
      price: 199,
      image:
        "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=1200&q=80",
      description:
        "Classic wooden family frame perfect for home wall decoration.",
    },
    {
      id: 2,
      name: "Modern Gallery Frame",
      category: "Gallery Frames",
      price: 199,
      image:
        "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=1200&q=80",
      description:
        "Modern art gallery frame designed for luxury interiors.",
    },
    {
      id: 3,
      name: "Floating Glass Frame",
      category: "Floating Frames",
      price: 199,
      image:
        "https://images.unsplash.com/photo-1510076857177-7470076d4098?auto=format&fit=crop&w=1200&q=80",
      description:
        "Stylish floating glass frame with modern transparent design.",
    },
    {
      id: 4,
      name: "College Memory Frame",
      category: "College Frames",
      price: 199,
      image:
        "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1200&q=80",
      description:
        "Special graduation and college memory frame for students and friends.",
    },
  ];

  const handleBuyNow = (product) => {
    setSelectedProduct(product);
    setShowPopup(true);
    setShowPaymentModal(true);

    setTimeout(() => {
      setShowPopup(false);
    }, 3000);
  };

  const handleGenerateReceipt = () => {
    if (customerName.trim() !== "" && paymentId.trim() !== "") {
      setShowReceipt(true);
      setShowPaymentModal(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 text-gray-900">
      <header className="bg-black text-white py-6 shadow-lg">
        <div className="max-w-7xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
          <div>
            <h1 className="text-4xl font-bold">THE GRID LIBRARY</h1>
            <p className="text-gray-300 mt-2">
              Premium Photo Frames For Every Beautiful Memory
            </p>
          </div>

          <div className="mt-4 md:mt-0 text-sm text-right">
            <p>Phone: 7995966131</p>
            <p>Email: pakalamahesh08@gmail.com</p>
            <p>UPI: 7995966131@ptsbi</p>
          </div>
        </div>
      </header>

      <section className="relative h-[420px] overflow-hidden">
        <img
          src="https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=1600&auto=format&fit=crop"
          alt="Frames"
          className="w-full h-full object-cover"
        />

        <div className="absolute inset-0 bg-black/50 flex items-center justify-center">
          <div className="text-center text-white px-4">
            <h2 className="text-5xl font-bold mb-4">
              Beautiful Frames Starting At Rs.199
            </h2>

            <p className="text-lg max-w-2xl mx-auto">
              Explore premium standard, gallery, floating, and college photo
              frames.
            </p>
          </div>
        </div>
      </section>

      <section className="max-w-7xl mx-auto px-4 py-14">
        <h2 className="text-3xl font-bold text-center mb-10">
          Featured Frames
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          {products.map((product) => (
            <div
              key={product.id}
              className="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition duration-300"
            >
              <img
                src={product.image}
                alt={product.name}
                className="w-full h-64 object-cover"
              />

              <div className="p-5">
                <h3 className="text-xl font-bold mb-2">{product.name}</h3>

                <p className="text-gray-600 text-sm mb-4">
                  {product.description}
                </p>

                <div className="flex items-center justify-between mb-4">
                  <span className="text-green-600 text-2xl font-bold">
                    Rs.{product.price}
                  </span>

                  <span className="bg-gray-200 text-sm px-3 py-1 rounded-full">
                    {product.category}
                  </span>
                </div>

                <button
                  onClick={() => handleBuyNow(product)}
                  className="w-full bg-black text-white py-3 rounded-xl hover:bg-gray-800 transition"
                >
                  Buy Now
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>

      {showPopup && selectedProduct && (
        <div className="fixed top-5 right-5 bg-green-600 text-white px-6 py-4 rounded-2xl shadow-2xl z-50">
          <h3 className="font-bold text-lg mb-1">
            Order Added Successfully
          </h3>

          <p>
            {selectedProduct.name} - Rs.{selectedProduct.price}
          </p>

          <p className="text-sm mt-1">
            Payment UPI: 7995966131@ptsbi
          </p>
        </div>
      )}

      {selectedProduct && (
        <section className="max-w-6xl mx-auto px-4 pb-16">
          <div className="bg-white rounded-3xl shadow-2xl overflow-hidden grid grid-cols-1 md:grid-cols-2">
            <img
              src={selectedProduct.image}
              alt={selectedProduct.name}
              className="w-full h-full object-cover"
            />

            <div className="p-8 flex flex-col justify-center">
              <h2 className="text-4xl font-bold mb-4">
                {selectedProduct.name}
              </h2>

              <p className="text-gray-600 text-lg mb-6">
                {selectedProduct.description}
              </p>

              <div className="flex items-center gap-4 mb-6">
                <span className="text-green-600 text-4xl font-bold">
                  Rs.{selectedProduct.price}
                </span>

                <span className="bg-gray-200 px-4 py-2 rounded-full text-sm">
                  {selectedProduct.category}
                </span>
              </div>

              <div className="space-y-3 text-gray-700">
                <p>Premium Quality Material</p>
                <p>Fast Delivery Available</p>
                <p>Secure UPI Payment</p>
                <p>Custom Designs Supported</p>
              </div>

              <button
                onClick={() => setShowPaymentModal(true)}
                className="mt-8 bg-black text-white py-4 rounded-2xl hover:bg-gray-800 transition text-lg font-semibold"
              >
                Proceed To Payment
              </button>
            </div>
          </div>
        </section>
      )}

      {showPaymentModal && (
        <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-3xl max-w-md w-full p-6 relative shadow-2xl">
            <button
              onClick={() => setShowPaymentModal(false)}
              className="absolute top-4 right-4 text-2xl font-bold text-gray-600 hover:text-black"
            >
              ×
            </button>

            <h2 className="text-3xl font-bold text-center mb-4">
              Scan & Pay
            </h2>

            <p className="text-center text-gray-600 mb-6">
              Scan the QR code using any UPI app
            </p>

            <div className="bg-gray-100 rounded-2xl p-4 border shadow-lg flex justify-center">
              <img
                src={qrCodeImage}
                alt="UPI QR Code"
                className="w-full max-w-xs rounded-2xl bg-white p-2"
              />
            </div>

            <div className="mt-6 space-y-4">
              <input
                type="text"
                placeholder="Enter Customer Name"
                value={customerName}
                onChange={(e) => setCustomerName(e.target.value)}
                className="w-full border rounded-xl p-3"
              />

              <input
                type="text"
                placeholder="Enter Payment ID"
                value={paymentId}
                onChange={(e) => setPaymentId(e.target.value)}
                className="w-full border rounded-xl p-3"
              />

              <button
                onClick={handleGenerateReceipt}
                className="w-full bg-green-600 text-white py-3 rounded-xl font-semibold hover:bg-green-700"
              >
                Generate Receipt
              </button>

              <div className="text-center">
                <p className="text-lg font-semibold">
                  UPI ID: 7995966131@ptsbi
                </p>

                <p className="text-gray-500 mt-2">
                  Account Holder: PAKALA MAHESH
                </p>
              </div>
            </div>
          </div>
        </div>
      )}

      {showReceipt && selectedProduct && (
        <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-3xl max-w-lg w-full p-8 shadow-2xl">
            <h2 className="text-4xl font-bold text-center mb-6 text-green-600">
              Payment Receipt
            </h2>

            <div className="space-y-4 text-lg">
              <div className="flex justify-between border-b pb-2">
                <span className="font-semibold">Customer Name:</span>
                <span>{customerName}</span>
              </div>

              <div className="flex justify-between border-b pb-2">
                <span className="font-semibold">Payment ID:</span>
                <span>{paymentId}</span>
              </div>

              <div className="flex justify-between border-b pb-2">
                <span className="font-semibold">Product:</span>
                <span>{selectedProduct.name}</span>
              </div>

              <div className="flex justify-between border-b pb-2">
                <span className="font-semibold">Amount Paid:</span>
                <span>Rs.{selectedProduct.price}</span>
              </div>

              <div className="flex justify-between border-b pb-2">
                <span className="font-semibold">Seller Name:</span>
                <span>PAKALA MAHESH</span>
              </div>

              <div className="flex justify-between border-b pb-2">
                <span className="font-semibold">Seller Mobile:</span>
                <span>7995966131</span>
              </div>
            </div>

            <button
              onClick={() => setShowReceipt(false)}
              className="mt-8 w-full bg-black text-white py-4 rounded-2xl hover:bg-gray-800 font-semibold"
            >
              Close Receipt
            </button>
          </div>
        </div>
      )}

      <section className="bg-white py-16">
        <div className="max-w-5xl mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-8">
            Admin Dashboard Preview
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-gray-100 rounded-2xl p-6 shadow">
              <h3 className="text-xl font-bold mb-2">Total Products</h3>
              <p className="text-4xl font-bold text-green-600">4</p>
            </div>

            <div className="bg-gray-100 rounded-2xl p-6 shadow">
              <h3 className="text-xl font-bold mb-2">Orders</h3>
              <p className="text-4xl font-bold text-blue-600">12</p>
            </div>

            <div className="bg-gray-100 rounded-2xl p-6 shadow">
              <h3 className="text-xl font-bold mb-2">Categories</h3>
              <p className="text-4xl font-bold text-purple-600">4</p>
            </div>
          </div>
        </div>
      </section>

      <footer className="bg-black text-white py-8 text-center">
        <p className="text-lg font-semibold">THE GRID LIBRARY</p>
        <p className="text-gray-400 mt-2">
          Copyright 2026. All Rights Reserved.
        </p>
      </footer>
    </div>
  );
}
