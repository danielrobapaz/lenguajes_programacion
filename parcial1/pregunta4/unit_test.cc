#include "vector.h"
#include <gtest/gtest.h>
#include <cmath>

TEST(vector, vectorIntSum) {
  Vector v1, v2, res;

  v1 = Vector{40, 11, 17};
  v2 = Vector{14, 21, 35};
  
  res = v1+v2;

  // Expect equality.
  EXPECT_EQ(res.x, 54);
  EXPECT_EQ(res.y, 32);
  EXPECT_EQ(res.z, 52);
}

TEST(vector, vectorFloatSum) {
  Vector v1, v2, res;

  v1 = Vector{11.1, 8.1, 34.1};
  v2 = Vector{7.5,22.8, 15.6};

  res = v1+v2;

  // Expect equality.
  EXPECT_EQ(res.x, 18.6);
  EXPECT_EQ(res.y, 30.9);
  EXPECT_EQ(res.z, 49.7);
}

TEST(vector, vectorIntSub) {
  Vector v1, v2, res;

  v1 = Vector{32, 15, 26};
  v2 = Vector{1, -8, -8};
  
  res = v1-v2;

  // Expect equality.
  EXPECT_EQ(res.x, 31);
  EXPECT_EQ(res.y, 23);
  EXPECT_EQ(res.z, 34);
}

TEST(vector, vectorFloatSub) {
  Vector v1, v2, res;

  v1 = Vector{49.8, -2.6, 6.6};
  v2 = Vector{17.0,2.6, 6.6};
  
  res = v1-v2;

  // Expect equality.
  EXPECT_EQ(res.x, 32.8);
  EXPECT_EQ(res.y, -5.2);
  EXPECT_EQ(res.z, 0);
}

TEST(vector, vectorIntDot) {
  Vector v1, v2;
  double res;

  v1 = Vector{12, 26, 44};
  v2 = Vector{-4, 63, -92};
  
  res = v1%v2;

  // Expect equality.
  EXPECT_EQ(res, (12*-4) + (26*63) + (44*-92));
}

TEST(vector, vectorFloatDot) {
  Vector v1, v2;
  double res;

  v1 = Vector{86.9, -3.8, 0};
  v2 = Vector{18.8,-9.7, 6.6};
  
  res = v1%v2;

  // Expect equality.
  EXPECT_EQ(res, (86.9*18.8) + (-3.8*-9.7) + (0*6.6));
}

TEST(vector, vectorDotNeutro) {
  Vector v1, v2, v3;

  v1 = Vector{5, -36, 1000000};
  v2 = Vector{18.8,-999999.7, 6.6};
  v3 = Vector{0, 0, 0};

  // Expect equality.
  EXPECT_EQ(v1%v3, 0);
  EXPECT_EQ(v2%v3, 0);
}

TEST(vector, vectorOrtogonalVectorialProduct) {
  Vector v1, v2;
  
  v1 = Vector{45, -9654, 40};
  v2 = Vector{52.9, 87, -5};

  EXPECT_EQ(v1%(v1*v2), 0);
}

TEST(vector, vectorParalelVectorialProduct) {
  Vector v1,v2, res;

  v1 = Vector{1, 3, 2};
  v2 = Vector{2, 6, 4};
  res = v1 * v2;
  
  EXPECT_EQ(res.x, 0);
  EXPECT_EQ(res.y, 0);
  EXPECT_EQ(res.z, 0);
}

TEST(vector, vectorNilpotentVectorialProduct) {
  Vector v1, v2, res;

  v1 = Vector{4.6, 5.6, 99999};
  v2 = Vector{4.6, 5.6, 99999};
  res = v1 * v2;

  EXPECT_EQ(res.x, 0);
  EXPECT_EQ(res.y, 0);
  EXPECT_EQ(res.z, 0);
}

TEST(vector, vectorVectorialProduct) {
  Vector v1, v2, res;
  
  v1 = Vector{4, 5, -9};
  v2 = Vector{-1000000, 0, -99};
  res = v1 * v2;

  EXPECT_EQ(res.x, -495);
  EXPECT_EQ(res.y, 9000396);
  EXPECT_EQ(res.z, 5000000);

}

TEST(vector, vectorNormInt) {
  Vector v1;
  
  v1 = Vector{27, -202, 69};

  EXPECT_EQ(&v1, sqrt(27*27 + -202*-202 + 69*69));
}

TEST(vector, vectorNormFloat) {
  Vector v1;
  
  v1 = Vector{33.27, -29.202, 3.14};

  EXPECT_EQ(&v1, sqrt(33.27*33.27 + -29.202*-29.202 + 3.14*3.14));
}

TEST (vector, vectorNormDot) {
  Vector v1;

  v1 = Vector{2, 434, 1942};

  EXPECT_EQ(&v1, sqrt(v1%v1));
}

TEST(vector, vectorSumEscalar) {
  Vector v1, res;

  v1 = Vector{-555, -999, -888};
  res = v1+87;

  EXPECT_EQ(res.x, -555+87);
  EXPECT_EQ(res.y, -999+87);
  EXPECT_EQ(res.z, -888+87);
}

TEST(vector, vectorSubEscalar) {
  Vector v1, res;

  v1 = Vector{75634, 0, -52345};
  res = v1-87;

  EXPECT_EQ(res.x, 75634-87);
  EXPECT_EQ(res.y, 0-87);
  EXPECT_EQ(res.z, -52345-87);
}

TEST(vector, vectorDivEscalar) {
  Vector v1, res;

  v1 = Vector{546123, 653345, -642345234};
  res = v1/87.0;

  EXPECT_EQ(res.x, 546123/87.0);
  EXPECT_EQ(res.y, 653345/87.0);
  EXPECT_EQ(res.z, -642345234/87.0);
}

TEST(vector, vectorMultEscalar) {
  Vector v1, res;

  v1 = Vector{-45923, 1234, -53};
  res = v1*87;

  EXPECT_EQ(res.x, -45923*87);
  EXPECT_EQ(res.y, 1234*87);
  EXPECT_EQ(res.z, -53*87);
}


TEST(vector, vectorOp1) {
  Vector v1, v2, v3, res;

  v1 = Vector{423, -65, 3};
  v2 = Vector{43, 0, 31};
  v3 = Vector{123, 2, -42131};
  res = v1 * v2 + v3;

  EXPECT_EQ(res.x, -1892);
  EXPECT_EQ(res.y, -12982);
  EXPECT_EQ(res.z, -39336); 
}

TEST(vector, vectorOp2) {
  Vector v1, v2, v3, res;

  v1 = Vector{423, -65, 3};
  v2 = Vector{43, 0, 31};
  v3 = Vector{123, 2, -421};
  res = (v2 + v2) * (v3 - v1);

  EXPECT_EQ(res.x, -4154);
  EXPECT_EQ(res.y, 17864);
  EXPECT_EQ(res.z, 5762); 
}

TEST(vector, vectorOp3) {
  Vector v1, res;

  v1 = Vector{0, 3, 4};
  res = (v1 * 3) + &v1;

  EXPECT_EQ(res.x, 5); 
  EXPECT_EQ(res.y, 14); 
  EXPECT_EQ(res.z, 17); 
}

TEST(vector, vectorOp4) {
  Vector v1, v2, v3, res;

  v1 = Vector{3, -65, 3};
  v2 = Vector{43, 0, 31};
  v3 = Vector{10, 2, -5};
  res = (v2 + v2) * (v3 % v1);

  EXPECT_EQ(res.x, -9890);
  EXPECT_EQ(res.y, 0);
  EXPECT_EQ(res.z, -7130); 
}