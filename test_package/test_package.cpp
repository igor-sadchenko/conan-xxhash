#include <xxhash32.h>
#include <xxhash64.h>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <string>


#define EXPECT_TRUE(arg) \
        do { \
            if(!(arg)) { \
                std::cerr << "Unexpected false at " \
                        << __FILE__ << ", " << __LINE__ << ", " << __func__ << ": " << #arg << ": \033[31mFAILED\033[0m\n"; \
                return -1; } \
            else { \
                std::cout << __FILE__ << ", " << __LINE__ << ", " << __func__ << ": \033[32mPASSED\033[0m\n"; } \
        } while(false);

// This is a simple example
int main()
{
    std::string email {"test@test.test"};

    std::uint32_t hash32 = XXHash32::hash(email.c_str(), email.size(), 0);
    EXPECT_TRUE(hash32 == 189115812u);

    std::uint64_t hash64 = XXHash64::hash(email.c_str(), email.size(), 0);
    EXPECT_TRUE(hash64 == 4937474057170619421ull);

    return 0;
}