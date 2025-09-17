import time
import sys

def factors_list(n):
    """Traditional function that returns all factors as a list"""
    results = []
    for i in range(1, n + 1):
        if n % i == 0:
            results.append(i)
    return results

def factors_gen(n):
    """Generator function that yields factors one by one"""
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

def test_full_computation(n):
    """Test when we need ALL factors - this is where your original test was"""
    print("=" * 50)
    print("TEST 1: Full Computation (All Factors)")
    print("=" * 50)
    
    # List version
    start = time.time()
    result_list = factors_list(n)
    list_time = time.time() - start
    
    # Generator version (with list() conversion - this is what you did)
    start = time.time()
    result_gen = list(factors_gen(n))
    gen_time = time.time() - start
    
    print(f"List version time: {list_time:.4f} seconds")
    print(f"Generator + list() time: {gen_time:.4f} seconds")
    print(f"Results equal: {result_list == result_gen}")
    print(f"Number of factors: {len(result_list)}")
    print(f"Memory - List: {sys.getsizeof(result_list)} bytes")
    print(f"Memory - Generator object: {sys.getsizeof(factors_gen(n))} bytes")
    
    if list_time < gen_time:
        print(f"✅ List is {gen_time/list_time:.1f}x faster (expected when converting all)")
    else:
        print(f"✅ Generator is {list_time/gen_time:.1f}x faster")

def test_early_termination(n, threshold=1000):
    """Test early termination - where generators really shine"""
    print("\n" + "=" * 50)
    print(f"TEST 2: Early Termination (First factor > {threshold})")
    print("=" * 50)
    
    # Generator version - stops early
    start = time.time()
    first_large_gen = None
    for factor in factors_gen(n):
        if factor > threshold:
            first_large_gen = factor
            break
    gen_time = time.time() - start
    
    # List version - computes all factors first
    start = time.time()
    all_factors = factors_list(n)
    first_large_list = None
    for factor in all_factors:
        if factor > threshold:
            first_large_list = factor
            break
    list_time = time.time() - start
    
    print(f"Generator (early stop): {gen_time:.6f} seconds")
    print(f"List (all factors): {list_time:.4f} seconds")
    print(f"Found factor: {first_large_gen}")
    print(f"Results equal: {first_large_gen == first_large_list}")
    
    if gen_time < list_time:
        print(f"🚀 Generator is {list_time/gen_time:.0f}x faster!")
    else:
        print(f"List is {gen_time/list_time:.1f}x faster")

def test_partial_consumption(n, limit=5):
    """Test getting only first few factors"""
    print("\n" + "=" * 50)
    print(f"TEST 3: Partial Consumption (First {limit} factors)")
    print("=" * 50)
    
    # Generator version - only computes what we need
    start = time.time()
    first_few_gen = []
    for i, factor in enumerate(factors_gen(n)):
        if i >= limit:
            break
        first_few_gen.append(factor)
    gen_time = time.time() - start
    
    # List version - computes all factors first
    start = time.time()
    all_factors = factors_list(n)
    first_few_list = all_factors[:limit]
    list_time = time.time() - start
    
    print(f"Generator (first {limit}): {gen_time:.6f} seconds")
    print(f"List (all then slice): {list_time:.4f} seconds")
    print(f"First {limit} factors: {first_few_gen}")
    print(f"Results equal: {first_few_gen == first_few_list}")
    
    if gen_time < list_time:
        print(f"🚀 Generator is {list_time/gen_time:.0f}x faster!")
    else:
        print(f"List is {gen_time/list_time:.1f}x faster")

def test_memory_efficiency(n):
    """Test memory usage comparison"""
    print("\n" + "=" * 50)
    print("TEST 4: Memory Usage")
    print("=" * 50)
    
    # Create instances
    gen = factors_gen(n)
    factors_list_result = factors_list(n)
    
    print(f"Generator object size: {sys.getsizeof(gen)} bytes")
    print(f"List with all factors: {sys.getsizeof(factors_list_result)} bytes")
    print(f"List elements total: {sum(sys.getsizeof(f) for f in factors_list_result)} bytes")
    
    memory_savings = sys.getsizeof(factors_list_result) / sys.getsizeof(gen)
    print(f"🔥 Generator uses {memory_savings:.1f}x less memory!")

def test_multiple_iterations(n):
    """Test when you need to iterate multiple times"""
    print("\n" + "=" * 50)
    print("TEST 5: Multiple Iterations")
    print("=" * 50)
    
    # List version - can iterate multiple times efficiently
    start = time.time()
    factors_list_result = factors_list(n)
    
    # Iterate 3 times
    for iteration in range(3):
        total = sum(factors_list_result)
    
    list_time = time.time() - start
    
    # Generator version - need to recreate for each iteration
    start = time.time()
    
    # Iterate 3 times
    for iteration in range(3):
        total = sum(factors_gen(n))  # Recreates generator each time
    
    gen_time = time.time() - start
    
    print(f"List (3 iterations): {list_time:.4f} seconds")
    print(f"Generator (3 iterations): {gen_time:.4f} seconds")
    
    if list_time < gen_time:
        print(f"✅ List is {gen_time/list_time:.1f}x faster for multiple iterations")
    else:
        print(f"Generator is {list_time/gen_time:.1f}x faster")

def main():
    print("🔍 GENERATOR vs LIST PERFORMANCE COMPARISON")
    print("Testing with n = 1000000000 (1 billion)")
    
    n = 1000000000
    
    # Test 1: Full computation (your original test)
    test_full_computation(n)
    
    # Test 2: Early termination (generators shine here)
    test_early_termination(n, threshold=1000)
    
    # Test 3: Partial consumption
    test_partial_consumption(n, limit=5)
    
    # Test 4: Memory efficiency
    test_memory_efficiency(n)
    
    # Test 5: Multiple iterations
    test_multiple_iterations(n)
    
    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)
    print("✅ Lists are better when:")
    print("   - You need ALL values")
    print("   - Multiple iterations over same data")
    print("   - Random access needed")
    print("   - Small datasets")
    print()
    print("🚀 Generators are better when:")
    print("   - You might not need all values")
    print("   - Early termination is common")
    print("   - Memory is constrained")
    print("   - Processing large datasets")
    print("   - One-time iteration")

if __name__ == "__main__":
    main()
