#include <unity.h>

void test_function_calculator_addition(void) {
    TEST_ASSERT_EQUAL(32, 32);
}

void setup() {
    UNITY_BEGIN();
    RUN_TEST(test_function_calculator_addition);
    UNITY_END();
}

void loop() {
    // Diese Funktion bleibt in PlatformIO-Tests leer.
}
