FROM archlinux:latest

# Update mirrors first
RUN pacman -Sy --noconfirm reflector && \
    reflector --country US --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist

# Update system
RUN pacman -Syu --noconfirm

# Install packages in smaller groups
RUN pacman -S --noconfirm base-devel git vim nano
RUN pacman -S --noconfirm wget curl sudo neovim

# Clean cache
RUN pacman -Scc --noconfirm

# Create user with sudo privileges
RUN useradd -m -G wheel -s /bin/bash archuser && \
    echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Set working directory
WORKDIR /workspace

# Switch to non-root user
USER archuser

# Keep container running
CMD ["bash"]
