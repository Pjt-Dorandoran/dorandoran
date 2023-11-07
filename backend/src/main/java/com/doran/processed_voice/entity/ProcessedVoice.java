package com.doran.processed_voice.entity;

import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;

import com.doran.content.entity.Content;
import com.doran.user.entity.User;
import com.doran.utils.common.Genders;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@Table(name = "processed_voice")
@RequiredArgsConstructor
public class ProcessedVoice {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "pv_id")
    private int id;
    //
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "content_id")
    @OnDelete(action = OnDeleteAction.CASCADE)
    private Content content;

    //유저 매핑
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    private User user;

    @Column(name = "voice_url", nullable = false)
    private String voiceUrl;

    @Column(name = "voice_gender", nullable = true)
    @Enumerated(EnumType.STRING)
    private Genders voiceGender;
}
