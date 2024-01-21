#include "MyMath.h"
#include "gtest/gtest.h"

TEST(MathTest, Add) { EXPECT_EQ(3, MyMath::add(1, 2)); }

TEST(MathTest, Subtract) { EXPECT_EQ(1, MyMath::subtract(2, 1)); }

TEST(MathTest, Multiply) { EXPECT_EQ(6, MyMath::multiply(2, 3)); }

TEST(MathTest, Divide) { EXPECT_EQ(2, MyMath::divide(6, 3)); }
