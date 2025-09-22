import { Resolver, Query, Mutation, Arg, Ctx } from 'type-graphql';

@Resolver()
export class UserResolver {
  @Query(() => String)
  users(): string {
    return 'Users GraphQL endpoint - Implementation in progress';
  }

  @Query(() => String)
  accessibilityProfile(@Arg('userId') userId: string): string {
    return `Accessibility profile for user ${userId} - Implementation in progress`;
  }

  @Mutation(() => String)
  updateAccessibilityProfile(
    @Arg('userId') userId: string,
    @Arg('preferences') preferences: string
  ): string {
    return `Updated accessibility profile for user ${userId}`;
  }
}