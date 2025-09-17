FROM archlinux:latest

# Update system and install packages
RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm base-devel git vim nano wget curl sudo neovim && \
    pacman -Scc --noconfirm

# Create user with sudo privileges
RUN useradd -m -G wheel -s /bin/bash archuser && \
    echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Set working directory
WORKDIR /workspace

# Switch to non-root user
USER archuser

# Keep container running
CMD ["bash"]
