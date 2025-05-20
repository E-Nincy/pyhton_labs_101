# Fix the variable assignment shown below.
# Can you see why using the multiple variable assignment can be tricky?
# A// YEs, because it's easy to accidentally swap values or misread which variable gets which value.
# Declared like this, it's easy to mix which is which.

dreams, profession = "flying", "programming"

dreams = "flying"
profession = "programming"

print(f"my dream is to {dreams}, but i currently work as a {profession}")
