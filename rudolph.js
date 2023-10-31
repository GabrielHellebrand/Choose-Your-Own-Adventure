function updateGameText(text) {
  gameText.innerText = text;
}

function updateOptions(option1Text, option2Text, option3Text) {
  option1.innerText = option1Text;
  option2.innerText = option2Text;
  option3.innerText = option3Text;
}

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Time delay effect
const a = 1000; // 1 second
const b = 50;   // 50 milliseconds

function intro() {
  const print1 = "That's great! Let's play!\n";
  setTimeout(() => {
    typeText(print1, () => {
      const print2 = "You are Santa's favorite elf nicknamed Santa's little helper and you're working in a sweatshop along with all of the other little elves.\n";
      setTimeout(() => {
        typeText(print2, () => {
          const print3 = "The Soviet Union National Anthem blasts on repeat in the North Pole sweatshop at a deafening volume.\n";
          setTimeout(() => {
            typeText(print3, () => {
              const print4 = "It hurts your little commie elf ears.\n";
              setTimeout(() => {
                typeText(print4, () => {
                  const print5 = "All is well in Santa's sweatshop, except for the fact that Rudolph recently has gotten into Santa's favorite bottle of vodka.\n";
                  setTimeout(() => {
                    typeText(print5, () => {
                      const print6 = "Since then Rudolph has become a heavy alcoholic and has gotten a very red nose from all of the drinking that he's been doing.\n";
                      setTimeout(() => {
                        typeText(print6, () => {
                          const print7 = "Rudolph with his nose so bright isn't flying any sleighs tonight.\n";
                          setTimeout(() => {
                            typeText(print7, () => {
                              const print8 = "One day, Rudolph stumbles into the elf sweatshop looking dazed and confused.\n";
                              setTimeout(() => {
                                typeText(print8, () => {
                                  const print9 = "Rudolph's very dizzy and seems to have lost his balance. He falls on all fours.\n";
                                  setTimeout(() => {
                                    typeText(print9, () => {
                                      const print10 = "From here you have three options.\n";
                                      setTimeout(() => {
                                        typeText(print10, () => {
                                          const print11 = "Option 1: BOOP RUDOLPH IN THE NOSE TO SEE IF IT CHANGES COLOR.\n";
                                          setTimeout(() => {
                                            typeText(print11, () => {
                                              const print12 = "Option 2: TAKE RUDOLPH TO THE VET FOR SUSPECTED ALCOHOL POISONING.\n";
                                              setTimeout(() => {
                                                typeText(print12, () => {
                                                  const print13 = "Option 3: TELL RUDOLPH TO GO INTO REHAB.\n";
                                                  setTimeout(() => {
                                                    typeText(print13, () => {
                                                      rl.question("Which option will you choose? [1/2/3]: ", (firstOption) => {
                                                        if (firstOption === "1") {
                                                          console.log();
                                                          option1();
                                                        } else if (firstOption === "2") {
                                                          console.log();
                                                          option2();
                                                        } else if (firstOption === "3") {
                                                          console.log();
                                                          option3();
                                                        } else {
                                                          const print14 = "Rudolph dies from alcohol poisoning.\n";
                                                          console.log();
                                                          typeText(print14, () => {
                                                            main();
                                                          });
                                                        }
                                                      });
                                                    }, b);
                                                  }, b);
                                                }, b);
                                              }, b);
                                            }, b);
                                          }, b);
                                        }, b);
                                      }, b);
                                    }, b);
                                  }, b);
                                }, b);
                              }, b);
                            }, b);
                          }, b);
                        }, b);
                      }, b);
                    }, b);
                  }, b);
                }, b);
              }, b);
            }, b);
          }, b);
        }, b);
      }, b);
    }, b);
  }, b);
}

function typeText(text, callback) {
  let index = 0;
  function typeCharacter() {
    if (index < text.length) {
      process.stdout.write(text[index]);
      index++;
      setTimeout(typeCharacter, b);
    } else {
      console.log();
      callback();
    }
  }
  typeCharacter();
}
function option1() {
    const print122 = "Unfortunately, Rudolph's nose did not change color.\nInstead, Rudolph boops you on the nose with his hooves, sending you to the hospital.\n";
    setTimeout(() => {
      typeText(print122, () => {
        const print123 = "You get no visitors in the hospital as no one is allowed outside of the sweatshop.\n";
        setTimeout(() => {
          typeText(print123, () => {
            const print124 = "One day, a visitor arrives.\n";
            setTimeout(() => {
              typeText(print124, () => {
                const print125 = "The visitor tries to recruit you into an MLM scheme selling essential oils.\n";
                setTimeout(() => {
                  typeText(print125, () => {
                    const print126 = "The visitor tells you that last month she made over a thousand dollars.\n";
                    setTimeout(() => {
                      typeText(print126, () => {
                        const print127 = "What do you do?\n";
                        setTimeout(() => {
                          typeText(print127, () => {
                            console.log();
                            const print128 = "Option 1: JOIN AN MLM SCHEME AND BECOME A #ELFBOSS.\n";
                            setTimeout(() => {
                              typeText(print128, () => {
                                const print129 = "Option 2: TELL THE VISITOR THAT THEY'VE GOT TO PUMP THOSE NUMBERS UP, THOSE ARE ROOKIE NUMBERS.\n";
                                setTimeout(() => {
                                  typeText(print129, () => {
                                    rl.question("Which path will you choose [1/2]: ", (fifthOption) => {
                                      if (fifthOption === "1") {
                                        console.log();
                                        option1_1();
                                      } else if (fifthOption === "2") {
                                        console.log();
                                        option1_2();
                                      }
                                    });
                                  }, b);
                                }, b);
                              });
                            }, b);
                          });
                        }, b);
                      }, b);
                    }, b);
                  });
                }, b);
              });
            }, b);
          });
        }, b);
      });
    }, b);
  }
  function option1_1() {
    const print130 = "You join the MLM and you magically recover from all of your ailments\nthanks to the power of those essential oils.\n";
    setTimeout(() => {
      typeText(print130, () => {
        const print131 = "You go back to Santa's sweatshop and now you only speak in annoying emojis.\n";
        setTimeout(() => {
          typeText(print131, () => {
            const print132 = "The essential oils have given you the power to change your face into emojis somehow.\n";
            setTimeout(() => {
              typeText(print132, () => {
                const print133 = "The only words you can speak in English are #bosself and #elfboss.\n";
                setTimeout(() => {
                  typeText(print133, () => {
                    const print134 = "Rudolph organizes an intervention for you and your newfound MLM.\n";
                    setTimeout(() => {
                      typeText(print134, () => {
                        const print135 = "Rudolph tells you that you have a problem.\n";
                        setTimeout(() => {
                          typeText(print135, () => {
                            const print136 = "Santa comes out of his office annoyed that the group chat for the North Pole has been filled with you\nsending annoying emojis and writing about how you have become a #bosself.\n";
                            setTimeout(() => {
                              typeText(print136, () => {
                                const print137 = "Santa's workshop casts a vote to banish you to the South Pole.\n";
                                setTimeout(() => {
                                  typeText(print137, () => {
                                    const print138 = "The vote is unanimous, and you are banished to the South Pole.\n";
                                    setTimeout(() => {
                                      typeText(print138, () => {
                                        const print139 = "You're alone with only penguins to keep you company, and Rudolph is still an alcoholic.\n";
                                        setTimeout(() => {
                                          typeText(print139, () => {
                                            main();
                                          });
                                        }, b);
                                      });
                                    }, b);
                                  });
                                }, b);
                              });
                            }, b);
                          });
                        }, b);
                      });
                    }, b);
                  });
                }, b);
              });
            }, b);
          });
        }, b);
      });
    }, b);
  }
  
  function option1_2() {
    const print141 = "The visitor wishes you the best and she hopes that you get well soon.\n";
    setTimeout(() => {
      typeText(print141, () => {
        const print142 = "The visitor leaves, that night you die alone and unloved.\n";
        setTimeout(() => {
          typeText(print142, () => {
            const print143 = "Unfortunately, Rudolph is still an alcoholic, and you die alone.\n";
            setTimeout(() => {
              typeText(print143, () => {
                console.log();
                main();
              });
            }, b);
          });
        }, b);
      });
    }, b);
  }
  
  function option2() {
    const print89 = "You take Rudolph to the vet.\n";
    setTimeout(() => {
      typeText(print89, () => {
        const print90 = "The vet tells you that Rudolph's liver and kidneys are almost completely destroyed from the amount of alcohol he's consumed.\n";
        setTimeout(() => {
          typeText(print90, () => {
            const print91 = "The vet recommends that you take Rudolph to Alcoholics Anonymous and have him change his ways.\n";
            setTimeout(() => {
              typeText(print91, () => {
                const print92 = "Rudolph tells the vet and you that that wasn't an option.\n";
                setTimeout(() => {
                  typeText(print92, () => {
                    const print93 = "Rudolph tells you, 'I need your liver, elf-man'.\n";
                    setTimeout(() => {
                      typeText(print93, () => {
                        const print94 = "The vet tells Rudolph to not be so hasty before asking if you could give Rudolph your liver and kidneys.\n";
                        setTimeout(() => {
                          typeText(print94, () => {
                            const print95 = "You tell the vet that he of all people should know that elves and reindeer aren't compatible when trading internal organs.\n";
                            setTimeout(() => {
                              typeText(print95, () => {
                                const print96 = "You take Rudolph to Alcoholics Anonymous.\n";
                                setTimeout(() => {
                                  typeText(print96, () => {
                                    const print97 = "You wait in the car for Rudolph to finish his Alcoholics Anonymous meeting, it's taking a long time.\n";
                                    setTimeout(() => {
                                      typeText(print97, () => {
                                        const print98 = "You decide to go into the meeting because you suspect that Rudolph is causing trouble and being a public menace.\n";
                                        setTimeout(() => {
                                          typeText(print98, () => {
                                            const print99 = "You go into the Alcoholics Anonymous meeting and find Rudolph flirting with a female reindeer.\n";
                                            setTimeout(() => {
                                              typeText(print99, () => {
                                                const print100 = "What do you do?\n";
                                                setTimeout(() => {
                                                  typeText(print100, () => {
                                                    console.log();
                                                    const print101 = "From here you have two options.\n";
                                                    setTimeout(() => {
                                                      typeText(print101, () => {
                                                        const print102 = "Option 1: LET RUDOLPH FLIRT WITH THE REINDEER.\n";
                                                        setTimeout(() => {
                                                          typeText(print102, () => {
                                                            const print103 = "Option 2: TELL THE REINDEER THAT RUDOLPH FORGOT HIS ANTI-ITCH CREAM.\n";
                                                            setTimeout(() => {
                                                              typeText(print103, () => {
                                                                rl.question("Which path will you choose [1/2]: ", (fourthOption) => {
                                                                  if (fourthOption === "1") {
                                                                    console.log();
                                                                    option2_1();
                                                                  }
                                                                  if (fourthOption === "2") {
                                                                    option2_2();
                                                                  }
                                                                });
                                                              }, b);
                                                            });
                                                          }, b);
                                                        });
                                                      }, b);
                                                    });
                                                  }, b);
                                                });
                                              }, b);
                                            });
                                          }, b);
                                        });
                                      }, b);
                                    });
                                  }, b);
                                });
                              }, b);
                            });
                          }, b);
                        });
                      }, b);
                    });
                  }, b);
                });
              }, b);
            });
          }, b);
        });
      }, b);
    }, b);
  }
  
  function option2_1() {
        const print104 = "Rudolph continues flirting with the female reindeer.\n";
        setTimeout(() => {
          typeText(print104, () => {
            const print105 = "A tough reindeer arrives and tells Rudolph to stop flirting with the female reindeer as that was his fiancé.\n";
            setTimeout(() => {
              typeText(print105, () => {
                const print106 = "Rudolph tells the guy, 'It's okay, I'm incredibly drunk.'\n";
                setTimeout(() => {
                  typeText(print106, () => {
                    const print107 = "The tough reindeer pulls out a gun and shoots Rudolph.\n";
                    setTimeout(() => {
                      typeText(print107, () => {
                        const print108 = "Rudolph dies, you and the other elves have a funeral.\n";
                        setTimeout(() => {
                          typeText(print108, () => {
                            console.log();
                            const print109 = "You couldn't save Rudolph from his alcoholism or himself.\n";
                            setTimeout(() => {
                              typeText(print109, () => {
                                console.log();
                                main();
                              });
                            }, b);
                          });
                        }, b);
                      });
                    }, b);
                  });
                }, b);
              });
            }, b);
          });
        }, b);
      }
  
  
  function option2_2() {
    const print111 = "The female reindeer told Rudolph that that wasn't a problem and that she had her own anti-itch cream.\n";
  setTimeout(() => {
    typeText(print111, () => {
      const print112 = "Rudolph vomits disgusted at the fact that the female reindeer he was flirting with carried anti-itch cream.\n";
      setTimeout(() => {
        typeText(print112, () => {
          const print113 = "Rudolph is extremely shallow.\n";
          setTimeout(() => {
            typeText(print113, () => {
              const print114 = "Rudolph tells you that he needs a drink to clear his head from this day of excitement.\n";
              setTimeout(() => {
                typeText(print114, () => {
                  const print115 = "Rudolph and you go to the bar.\n";
                  setTimeout(() => {
                    typeText(print115, () => {
                      const print116 = "The two of you drink excessively.\n";
                      setTimeout(() => {
                        typeText(print116, () => {
                          console.log();
                          const print117 = "The next morning,\n";
                          setTimeout(() => {
                            typeText(print117, () => {
                              console.log();
                              const print118 = "You wake up dazed and confused in a bathtub filled with ice.\n";
                              setTimeout(() => {
                                typeText(print118, () => {
                                  const print119 = "You shout at the top of your lungs, 'Rudolph where's my kidneys?'\n";
                                  setTimeout(() => {
                                    typeText(print119, () => {
                                      console.log();
                                      const print120 = "Not only did you not save Rudolph from his alcoholism but you lost your kidneys as well.\n";
                                      setTimeout(() => {
                                        typeText(print120, () => {
                                          console.log();
                                          main();
                                        });
                                      }, b);
                                    });
                                  }, b);
                                });
                              }, b);
                            });
                          }, b);
                        });
                      }, b);
                    });
                  }, b);
                });
              }, b);
            });
          }, b);
        });
      }, b);
    });
  }, b);
}

function typeText(text) {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log(text);
        resolve();
      }, 1000); // Adjust the timeout duration as needed
    });
  }
  
  async function option3() {
    await typeText("Rudolph tells you that he doesn't want to go to rehab. You tell Rudolph that he doesn't have a choice in the matter.");
    await typeText("You take Rudolph to alcoholics anonymous.");
    await typeText("Rudolph leaves you in the car but makes sure to leave the window slightly open as it's a hot day of twenty degrees below zero.");
    await typeText("It's been a while, and you decide to check up on Rudolph to make sure he hasn't gotten into trouble yet.");
    await typeText("As he often does...");
    await typeText("You go into the Alcoholics Anonymous meeting and find Rudolph hitting on a female reindeer asking for her number.");
    await typeText("What do you do.");
    
    console.log();
    
    await typeText("Option 1: TAKE RUDOLPH AND YOURSELF BACK TO THE NORTH POLE AND TELL SANTA THERE'S NO HOPE FOR RUDOLPH TO RECOVER FROM HIS VULGAR ALCOHOLISM.");
    await typeText("Option 2: TELL THE REINDEER THAT RUDOLPH WAS FLIRTING WITH THAT RUDOLPH FORGOT HIS ANTI ITCH CREAM.");
    await typeText("Option 3: JOIN AN MLM SCHEME AND BECOME A #ELFBOSS.");
    await typeText("Option 4: BOOP RUDOLPH ON THE NOSE TO SEE IF IT CHANGES COLOR.");
    await typeText("Option 5: TAKE RUDOLPH TO THE VET.");
    
    console.log();
    
    const second_option = prompt("Which path would you choose? [1/2/3/4/5]: ");
    
    if (second_option === "2") {
      option2_2();
    } else if (second_option === "3") {
      option1_1();
    } else if (second_option === "4") {
      option1();
    } else if (second_option === "5") {
      option2();
    } else {
      await typeText("Going back to the North Pole, Santa waits for you and Rudolph at the sweat shop.");
      await typeText("Santa's arms are folded, he's bald, covered in tattoos, yoked, and has a large beard.");
      await typeText("'Where have the two of you been...?'");
      await typeText("Rudolph tells Santa you were the one who stole his vodka and that Rudolph caught you red-handed.");
      await typeText("Everything was okay though because Rudolph being the good reindeer that he was, was taking you to alcoholics anonymous.");
      await typeText("Santa tells you and Rudolph, 'I'm not angry, just disappointed.'");
      await typeText("You go into Santa's sweatshop, Soviet music blaring, and you start making toys.");
      await typeText("You couldn't believe that Rudolph would betray you like that and after everything you did for him too.");
      await typeText("You are no longer Santa's favorite little Elf.");
    
      console.log();
    
      await typeText("Later, a neighbor elf is struggling to put together a toy jack in the box.");
      await typeText("One of the elf supervisors tells the neighbor elf that he's behind schedule.");
      await typeText("The Elf tells him that he'll do better next time.");
    
      console.log();
    
      const third_option = prompt("Which path would you take [1/2]: ");
    
      if (third_option === "1") {
        option3_1();
      } else if (third_option === "2") {
        option3_2();
      } else {
        await typeText("Santa is outside having just bought a new Mercedes and doing donuts on the snow.");
        await typeText("Unfortunately, the traction on the tires isn't enough, and Santa's car spins out of control, killing everyone.");
      }
    }
  }
  function option3_1() {
    const print41 = "You stand up for the struggling Elf and tell the supervisor that you could help him catch up.\n";
    setTimeout(() => {
      typeText(print41, () => {
        const print42 = "The Elf supervisor tells you that he'll allow this but that he will become your responsibility and that if you don't deliver...\n";
        setTimeout(() => {
          typeText(print42, () => {
            const print43 = "Santa's not going to give you any milk and cookies this year.\n";
            setTimeout(() => {
              typeText(print43, () => {
                const print44 = "dum dum dum.\n";
                setTimeout(() => {
                  typeText(print44, () => {
                    const print45 = "You help the elf make toys, and he tells you, 'Santa is not the jolly old man we all think he is.'\n";
                    setTimeout(() => {
                      typeText(print45, () => {
                        const print46 = "You ask, 'what makes you say that?'\n";
                        setTimeout(() => {
                          typeText(print46, () => {
                            console.log();
                            const print47 = "The elf tells you, 'Before every Christmas, Santa gets two large bags of money from bald men covered in tattoos.'\n";
                            setTimeout(() => {
                              typeText(print47, () => {
                                const print48 = "You ask how much money Santa has in the bags.\n";
                                setTimeout(() => {
                                  typeText(print48, () => {
                                    const print49 = "You're new elf friend tells you, 'I don't know, he measures money in the amount of bags, not dollars.'\n";
                                    setTimeout(() => {
                                      typeText(print49, () => {
                                        const print50 = "The elf tells you that he's also seen Santa have two lists, those who are naughty and those who are nice.\n";
                                        setTimeout(() => {
                                          typeText(print50, () => {
                                            const print51 = "You tell your elf friend, 'yeah, everyone knows that.'\n";
                                            setTimeout(() => {
                                              typeText(print51, () => {
                                                const print52 = "You're elf friend tells you, 'Do you know anyone who's ever been on the naughty list?'\n";
                                                setTimeout(() => {
                                                  typeText(print52, () => {
                                                    const print53 = "You shake your head no. You're elf friend tells you that you know them, they just die under mysterious circumstances or disappear, or they have their photos and any mention of them erased from history.\n";
                                                    setTimeout(() => {
                                                      typeText(print53, () => {
                                                        const print54 = "You're elf friend believes that Santa is in the Russian mafia and is using the North Pole as a front for money laundering.\n";
                                                        setTimeout(() => {
                                                          typeText(print54, () => {
                                                            const print55 = "You tell the elf that you doubt that Santa has any mafia connections but that it was good talking to him.\n";
                                                            setTimeout(() => {
                                                              typeText(print55, () => {
                                                                console.log();
                                                                const print56 = "The next day,\n";
                                                                setTimeout(() => {
                                                                  typeText(print56, () => {
                                                                    const print57 = "You're elf buddy died by suicide last night by shooting himself in the back of the head.\n";
                                                                    setTimeout(() => {
                                                                      typeText(print57, () => {
                                                                        const print58 = "You launch a secret investigation into Santa Claus's office, setting up spy cameras, and tracking Santa's whereabouts at all times.\n";
                                                                        setTimeout(() => {
                                                                          typeText(print58, () => {
                                                                            const print59 = "Upon investigating the files and tapes, you discover that Santa's been talking to a guy named Ivan on the phone in Russian about the money laundering scheme.\n";
                                                                            setTimeout(() => {
                                                                              typeText(print59, () => {
                                                                                const print60 = "You go to the police to tell them what you've found.\n";
                                                                                setTimeout(() => {
                                                                                  typeText(print60, () => {
                                                                                    const print61 = "Unfortunately, none of the officers at the time speak any Russian.\n";
                                                                                    setTimeout(() => {
                                                                                      typeText(print61, () => {
                                                                                        const print62 = "Detective Alexei Petrov checks into the police station, he is not able to speak fluent Russian. However, Hank from accounting is able to, you talk to Hank. He listens to the phone conversation and is able to understand everything.\n";
                                                                                        setTimeout(() => {
                                                                                          typeText(print62, () => {
                                                                                            const print63 = "Hank tells the officers that sure enough Santa Claus was using his workshop as a front to launder money for the mob.\n";
                                                                                            setTimeout(() => {
                                                                                              typeText(print63, () => {
                                                                                                const print64 = "Santa gets arrested, and Hank thanks you for the fact that you stopped a major Russian Mafia scheme.\n";
                                                                                                setTimeout(() => {
                                                                                                  typeText(print64, () => {
                                                                                                    const print65 = "Rudolph, after hearing the news of Santa's Russian mob connection, tells you that he promises that he'll never drink again.\n";
                                                                                                    setTimeout(() => {
                                                                                                      typeText(print65, () => {
                                                                                                        console.log();
                                                                                                        const print66 = "Thanks for playing! You've won the game!\n";
                                                                                                        setTimeout(() => {
                                                                                                          typeText(print66, () => {
                                                                                                            console.log();
                                                                                                            console.log();
                                                                                                            console.log();
                                                                                                          });
                                                                                                        }, b);
                                                                                                      });
                                                                                                    }, b);
                                                                                                  });
                                                                                                }, b);
                                                                                              });
                                                                                            }, b);
                                                                                          });
                                                                                        }, b);
                                                                                      });
                                                                                    }, b);
                                                                                  });
                                                                                }, b);
                                                                              });
                                                                            }, b);
                                                                          });
                                                                        }, b);
                                                                      });
                                                                    }, b);
                                                                  });
                                                                }, b);
                                                              });
                                                            }, b);
                                                          });
                                                        }, b);
                                                      });
                                                    }, b);
                                                  });
                                                }, b);
                                              });
                                            }, b);
                                          });
                                        }, b);
                                      });
                                    }, b);
                                  });
                                }, b);
                              });
                            }, b);
                          });
                        }, b);
                      });
                    }, b);
                  });
                }, b);
              });
            }, b);
          });
        }, b);
      });
    }, b);
  }
    
  const print68 = "The Elf supervisor tells him that there isn't going to be a next time before pulling out a gun.\n";
  setTimeout(() => {
    typeText(print68, () => {
      const print69 = "The elf supervisor shoots the elf and tells you and the other elves to clean up the mess before Santa arrives.\n";
      setTimeout(() => {
        typeText(print69, () => {
          const print70 = "You and the other elves find a place to bury the elf body in the elf graveyard outside of the sweatshop.\n";
          setTimeout(() => {
            typeText(print70, () => {
              const print71 = "Santa arrives at the sweatshop and announces the bad news that Blitzen has broken his leg.\n";
              setTimeout(() => {
                typeText(print71, () => {
                  const print72 = "However, due to helping you with your alcoholism, Santa has decided to reward Rudolph by having him become the new leader of the sleigh.\n";
                  setTimeout(() => {
                    typeText(print72, () => {
                      const print73 = "All of the elves cheer at this good news, and they tell you that Rudolph is such a good reindeer for helping you with your alcoholism.\n";
                      setTimeout(() => {
                        typeText(print73, () => {
                          console.log();
                          const print74 = "Christmas Eve arrives.\n";
                          setTimeout(() => {
                            typeText(print74, () => {
                              const print75 = "Rudolph is incredibly drunk, having had a full bottle of Jack Daniels, a bottle of fireball whiskey, and a large soda.\n";
                              setTimeout(() => {
                                typeText(print75, () => {
                                  const print76 = "Santa asks if Rudolph was, 'Ready to lead the sleigh tonight?'\n";
                                  setTimeout(() => {
                                    typeText(print76, () => {
                                      const print77 = "Rudolph replied, 'Santa as I'll ever be, ready.\n";
                                      setTimeout(() => {
                                        typeText(print77, () => {
                                          const print78 = "There's no doubt about it, Rudolph was incredibly drunk.\n";
                                          setTimeout(() => {
                                            typeText(print78, () => {
                                              const print79 = "Santa pats Rudolph on the antlers and tells him, 'I like your enthusiasm Rudolph.'\n";
                                              setTimeout(() => {
                                                typeText(print79, () => {
                                                  console.log();
                                                  const print80 = "Midnight arrives, and Santa loads the sleigh.\n";
                                                  setTimeout(() => {
                                                    typeText(print80, () => {
                                                      const print81 = "Takeoff is a little shaky, but they manage to get their footing and fly straight. Santa asked if everything was okay up there.\n";
                                                      setTimeout(() => {
                                                        typeText(print81, () => {
                                                          const print82 = "They fly through New York City, however there are a lot of skyscrapers, and Rudolph is feeling very dizzy.\n";
                                                          setTimeout(() => {
                                                            typeText(print82, () => {
                                                              const print83 = "They are heading for the Empire State Building, Santa realizes too late that Rudolph is drunk.\n";
                                                              setTimeout(() => {
                                                                typeText(print83, () => {
                                                                  const print84 = "Santa says, 'Ho, ho... no' as the sleigh crashes into the Empire State Building. Killing Santa and all of the reindeer.\n";
                                                                  setTimeout(() => {
                                                                    typeText(print84, () => {
                                                                      const print85 = "Later, a news report announces that Santa's been killed after a deadly crash into the Empire State Building.\n";
                                                                      setTimeout(() => {
                                                                        typeText(print85, () => {
                                                                          const print86 = "It is discovered that one of Santa's reindeer, Rudolph, was found to have been very drunk at the time, his blood alcohol content being off the charts.\n";
                                                                          setTimeout(() => {
                                                                            typeText(print86, () => {
                                                                              const print87 = "Another news report states that Santa allegedly had ties with the Russian mafia who would use Santa's workshop as a front to launder money.\n";
                                                                              setTimeout(() => {
                                                                                typeText(print87, () => {
                                                                                  console.log();
                                                                                  const print88 = "Thanks for playing, you've completed the game, play again to see if you get a different ending from last time.\n";
                                                                                  setTimeout(() => {
                                                                                    typeText(print88, () => {
                                                                                      console.log();
                                                                                      console.log();
                                                                                      console.log();
                                                                                      main();
                                                                                    });
                                                                                  }, b);
                                                                                });
                                                                              }, b);
                                                                            });
                                                                          }, b);
                                                                        });
                                                                      }, b);
                                                                    });
                                                                  }, b);
                                                                });
                                                              }, b);
                                                            });
                                                          }, b);
                                                        });
                                                      }, b);
                                                    });
                                                  }, b);
                                                });
                                              }, b);
                                            });
                                          }, b);
                                        });
                                      }, b);
                                    });
                                  }, b);
                                });
                              }, b);
                            });
                          }, b);
                        });
                      }, b);
                    });
                  }, b);
                });
              }, b);
            });
          }, b);
        });
      }, b);
    });
  }, b);
  function main() {
  console.log('\n\n');
  console.log('      ################################');
  console.log('      #                              #');
  console.log('      # Rudolph The Drunken Reindeer #');
  console.log('      #                              #');
  console.log('      ################################');
  console.log('\n\n');
  const startGame = prompt('Hello, do you want to play a game? [y/n]: ');

  if (startGame.toLowerCase() === 'n') {
    console.log('Ok bye.');
    setTimeout(() => {
      // Insert exit logic here or do nothing to exit the program
    }, 3000);
  } else if (startGame.toLowerCase() === 'y') {
    intro();
  }
}