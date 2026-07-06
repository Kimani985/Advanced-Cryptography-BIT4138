print("=" * 55)
print("      PUBLIC KEY INFRASTRUCTURE (PKI) COMPONENTS")
print("=" * 55)

components = {
    "Certificate Authority (CA)": "Issues and signs digital certificates.",
    "Registration Authority (RA)": "Verifies the identity of certificate applicants.",
    "Digital Certificate": "Binds a public key to the owner's identity.",
    "Certificate Repository": "Stores and distributes digital certificates.",
    "End User": "Uses certificates for secure communication."
}

for component, description in components.items():
    print(f"\n{component}")
    print(f"  -> {description}")

print("\nPKI component identification completed successfully.")